#!/usr/bin/env python

"""
Fenced Code Tabs Extension for Python Markdown
=========================================

This extension generates Bootstrap HTML Tabs for consecutive fenced code blocks

See <https://github.com/yacir/markdown-fenced-code-tabs> for documentation.

Copyright © 2017-present [Yassir Barchi](https://github.com/yacir).

License: [MIT](https://opensource.org/licenses/MIT)
"""

from __future__ import absolute_import
from __future__ import unicode_literals

from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
from markdown.extensions.codehilite import CodeHilite, CodeHiliteExtension
from markdown.extensions.codehilite import parse_hl_lines

import re
import os
import sys
from time import time
from collections import deque
from collections import OrderedDict as odict

from htmlmin import minify
from jinja2 import Environment, FileSystemLoader

from . import util
from .tab import TabItem
from .tab import TabGroup

FENCED_CODE_BLOCK_REGEX = re.compile(r'''
    (?P<fence>^(?:~{3,}|`{3,}))[ ]*  # Opening ``` or ~~~
    (\{?\.?(?P<lang>[\w#.+-]*))?[ ]*    # Optional {, and lang
    # Optional highlight lines, single- or double-quote-delimited
    (hl_lines=(?P<quot>"|')(?P<hl_lines>.*?)(?P=quot))?[ ]*
    # Optional tab label, single- or double-quote-delimited
    (fct_label=(?P<fct_quot>"|')(?P<fct_label>.*?)(?P=fct_quot))?[ ]*
    }?[ ]*\n                                # Optional closing }
    (?P<code>.*?)(?<=\n)
    (?P=fence)[ ]*$''', re.MULTILINE | re.DOTALL | re.VERBOSE)

PARAM_REGEXES = odict((
    ('hl_lines', re.compile(r'''hl_lines=(?P<quot>"|')(?P<hl_lines>.*?)(?P=quot)''')),
    ('fct_label', re.compile(r'''fct_label=(?P<quot>"|')(?P<fct_label>.*?)(?P=quot)''')),
))


class CodeTabsPreprocessor(Preprocessor):

    def __init__(self, md, config=None):
        self.items = deque()

        self.config = config
        self.codehilite_config = None

        j2_env = Environment(loader=FileSystemLoader(util.get_current_path()), trim_blocks=True)
        self.template = j2_env.get_template(config['template'])

        self._setup_placeholder()

        super(CodeTabsPreprocessor, self).__init__(md)

    def _setup_placeholder(self):
        current_time = time()
        self.tab_placeholder = '<!-- {0}__code_tab__{{0}} -->'.format(current_time)
        self.tab_placeholder_regex = re.compile('<!-- {0}__code_tab__([0-9]+) -->'.format(current_time))

    def _get_codehilite_config(self):
        for ext in self.markdown.registeredExtensions:
            if isinstance(ext, CodeHiliteExtension):
                return ext.config

        return None

    def _parse_code_blocks(self, text):
        fitered_text = util.filter_content(text)

        while True:
            m = FENCED_CODE_BLOCK_REGEX.search(fitered_text)
            if m:

                first_line = fitered_text[m.start():].split('\n')[0]

                kwargs = {}
                for param, regex in PARAM_REGEXES.items():
                    param_m = regex.search(first_line)
                    if param_m:
                        if param_m.group(param):
                            kwargs[param] = param_m.group(param)
                        elif (not param_m.group(param) is None) and param in PARAM_DEFAULTS:
                            kwargs[param] = PARAM_DEFAULTS[param]
                        else:
                            raise Exception("{} needs an argument within \n{}".format(param, first_line))

                tab_lang = ''
                tab_title = ''

                if m.group('lang') and m.group('lang') not in PARAM_REGEXES:
                    tab_lang = m.group('lang')
                    tab_title = tab_lang

                if kwargs.get('fct_label'):
                    tab_title = kwargs.get('fct_label')

                code = self._highlite_code(tab_lang, m.group('code'), {'hl_lines': kwargs.get('hl_lines')})

                self.items.append(TabItem(tab_title, tab_lang, code))

                placeholder = self.tab_placeholder.format(len(self.items) - 1)

                fitered_text = '{}\n{}\n{}'.format(fitered_text[:m.start()], placeholder, fitered_text[m.end():])

            else:
                break

        return fitered_text

    def _render_code_tabs(self, text):
        transformed_lines = ''
        lines = text.split('\n')

        groups_count = 0
        tab_group_count = 0
        first_tab_index = None

        for line in lines:
            m = self.tab_placeholder_regex.search(line)
            if m:
                if first_tab_index is None:
                    first_tab_index = m.group(1)

                tab_group_count += 1
                continue
            else:

                # We have a non tab save to the tab set so let's aggregate
                # the tabs into a tab set and generate the corresponding HTML
                if len(line.strip()) != 0 and first_tab_index is not None:
                    tab_group = TabGroup(str(groups_count))

                    for _ in range(0, tab_group_count):
                        tab_group.add_tab(self.items.popleft())

                    group_html = self._generate_group_html_code(tab_group)
                    transformed_lines += '\n' + self.markdown.htmlStash.store(group_html, safe=True) + '\n\n'

                    groups_count += 1
                    first_tab_index = None
                    tab_group_count = 0

                transformed_lines += line + '\n'

        # If there are any remaining tabs enclose them in a final last tab set
        if self.items:
            tab_group = TabGroup(str(groups_count))

            while self.items:
                tab_group.add_tab(self.items.popleft())

            group_html = self._generate_group_html_code(tab_group)
            transformed_lines += '\n' + self.markdown.htmlStash.store(group_html, safe=True) + '\n\n'

        return transformed_lines

    def _generate_group_html_code(self, group):
        group_html = self.template.render(
            config=self.config,
            headers=group.get_headers(),
            contents=group.get_contents(),
            group_id=group.get_id()
        )

        if (sys.version_info > (3, 0)):
            return minify(group_html, remove_empty_space=True, remove_comments=True)
        else:
            return minify(group_html.decode("utf-8"), remove_empty_space=True, remove_comments=True)

    def _highlite_code(self, lang, code, options):
        if self.codehilite_config:
            highliter = CodeHilite(
                code,
                linenums=self.codehilite_config['linenums'][0],
                guess_lang=self.codehilite_config['guess_lang'][0],
                css_class=self.codehilite_config['css_class'][0],
                style=self.codehilite_config['pygments_style'][0],
                lang=(lang or None),
                noclasses=self.codehilite_config['noclasses'][0],
                hl_lines=parse_hl_lines(options['hl_lines'])
            )
            return highliter.hilite()

        return '<pre><code class="{}">{}</code></pre>'.format(lang, util.escape(code))

    def run(self, lines):
        self.codehilite_config = self._get_codehilite_config()
        parsed_lines = self._parse_code_blocks('\n'.join(lines))
        return self._render_code_tabs(parsed_lines).split('\n')


class CodeTabsExtension(Extension):

    def __init__(self, *args, **kwargs):
        # Default config
        self.config = {
            'single_block_as_tab': [False, 'Render a single code block as a tab'],
            'active_class': ['active', 'TODO'],
            'template': ['default', 'TODO'],
        }

        super(CodeTabsExtension, self).__init__(*args, **kwargs)

    def _get_template_file_name(self, name):
        template = 'default'
        templates = ['bootstrap3', 'bootstrap4']

        if name in templates:
            template = name

        return "{}-{}".format(template, 'template.html')

    def extendMarkdown(self, md, md_globals):
        self.setConfig('single_block_as_tab', util.to_bool(
            self.getConfig('single_block_as_tab')
        ))

        template_file = self.getConfig('template')
        template_file_name = self._get_template_file_name(template_file)
        self.setConfig('template', template_file_name)

        md.registerExtension(self)

        # Add CodeTabsPreprocessor to the Markdown instance.
        md.preprocessors.add('fenced_code_block', CodeTabsPreprocessor(md, self.getConfigs()), '>normalize_whitespace')


def makeExtension(*args, **kwargs):
    return CodeTabsExtension(*args, **kwargs)
