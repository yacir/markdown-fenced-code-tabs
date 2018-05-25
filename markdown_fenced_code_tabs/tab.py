"""
Tab related objects.

Fenced Code Tabs Extension for Python Markdown
This extension generates Bootstrap HTML Tabs for consecutive fenced code blocks

See <https://github.com/yacir/markdown-fenced-code-tabs> for documentation.

Copyright © 2017-present [Yassir Barchi](https://github.com/yacir).

License: [MIT](https://opensource.org/licenses/MIT)
"""

import random
import string

from collections import deque

from . import util


class TabItem(object):

    def __init__(self, title, lang, code):
        self.title = title
        self.lang = lang
        self.code = code

    def get_title(self):
        return self.title

    def get_lang(self):
        return self.lang

    def get_code(self):
        return self.code


class TabGroup(object):

    
    GROUP_ID = 'tab-group-{}'   
    #group-0
    TAB_ID = '{}-{}_{}'
    #group-0_0-python'
    RANDOM_ID_CHAR_LENGTH = 15

    def __init__(self, group_id):
        self.id = self.GROUP_ID.format(group_id)
        self.headers = deque()
        self.contents = deque()

    def add_tab(self, tab):
        index = len(self.headers)
        tab_id = self._get_tab_id(tab, str(index))
        self.headers.append({'id': tab_id, 'lang': tab.get_lang(), 'title': tab.get_title()})
        self.contents.append({'id': tab_id, 'lang': tab.get_lang(), 'code': tab.get_code()})

    def get_id(self):
        return self.id

    def get_headers(self):
        return self.headers

    def get_contents(self):
        return self.contents

    def _get_tab_id(self, tab, index):
        tab_lang = tab.get_lang()

        if tab_lang is None or not tab_lang.strip():
            tab_lang = util.random_string(self.RANDOM_ID_CHAR_LENGTH)

        return self.TAB_ID.format(self.id, index, tab_lang)
