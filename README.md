[![PyPI][pypi-image]][pypi-link]

  [pypi-image]: https://img.shields.io/pypi/v/markdown-fenced-code-tabs.svg
  [pypi-link]: https://pypi.python.org/pypi/markdown-fenced-code-tabs
  
# Markdown Code Tabs Extension

Generates Bootstrap HTML Tabs for Consecutive Markdown Fenced Code Blocks

```md
    ## Tabs 

    ```curl
    $ curl -O wget http://example.com/pk.zip
    ```

    ```wget
    $ wget http://example.com/pk.zip
    ```

    ## Single block

    ```
    $ ls -lisa
    ```
```

Becomes: 

![Generated result](docs/images/img1.png)

## Installation

Install the latest version with `pip`:
```sh
pip install markdown-fenced-code-tabs
```

## MkDocs Usage

```yml
markdown_extensions:
  - markdown_fenced_code_tabs:
      single_block_as_tab: True
```

## Options

### `single_block_as_tab`
If `True`, the extension will render a single code block as a tab. Default is `False`.

`single_block_as_tab: True` generates:

![True single_block_as_tab](docs/images/img2.png)

`single_block_as_tab: False` generates:

![False single_block_as_tab](docs/images/img3.png)

## License

MIT License

Copyright (c) 2017 Yassir Barchi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.