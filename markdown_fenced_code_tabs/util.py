"""
General utilities.

Fenced Code Tabs Extension for Python Markdown
This extension generates Bootstrap HTML Tabs for consecutive fenced code blocks

See <https://github.com/yacir/markdown-fenced-code-tabs> for documentation.

Copyright © 2017-present [Yassir Barchi](https://github.com/yacir).

License: [MIT](https://opensource.org/licenses/MIT)
"""

import os
import random
import string


def to_bool(param):
    the_bool = param

    if isinstance(param, str):
        the_bool = False if param.lower() is 'false' else True

    return the_bool

def filter_content(content):
    string_block = content.replace(u'\u2018', '&lsquo;')
    string_block = string_block.replace(u'\u2019', '&rsquo;')
    string_block = string_block.replace(u'\u201c', '&ldquo;')
    string_block = string_block.replace(u'\u201d', '&rdquo;')
    string_block = string_block.replace(u'\u2013', '&ndash;')
    string_block = string_block.replace(u'\xa0', '')

    try:
        string_block = string_block.decode('ascii', 'remove')
    except:
        string_block = content

    return string_block

def escape(txt):
    txt = txt.replace('&', '&amp;')
    txt = txt.replace('<', '&lt;')
    txt = txt.replace('>', '&gt;')
    txt = txt.replace('"', '&quot;')
    return txt

def random_string(length):
    return ''. join(
                random.SystemRandom().choice(
                    string.ascii_lowercase + string.digits
                ) for _ in range(length)
            )

def get_file_content(file_path):
    file_self = open(file_path)
    str_content = file_self.read()
    file_self.close()
    return str_content

def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))
