[![PyPI][pypi-image]][pypi-link]

  [pypi-image]: https://img.shields.io/pypi/v/markdown-fenced-code-tabs.svg
  [pypi-link]: https://pypi.python.org/pypi/markdown-fenced-code-tabs

# Markdown Code Tabs Extension

Generates Bootstrap HTML Tabs for Consecutive Markdown Fenced Code Blocks

```md
    ```http
    GET / HTTP/1.1
    User-Agent: MyClient/1.0.0
    Accept: application/vnd.travis-ci.2+json
    Host: api.travis-ci.org

    HTTP/1.1 200 OK
    Content-Type: application/json

    {"hello":"world"}
    ```

    ```shell
    $ travis raw /
    {"hello":"world"}
    ```

    ```ruby
    require 'travis'

    # You usually don't want to fire API requests manually
    client = Travis::Client.new
    client.get_raw('/') # => {"hello"=>"world"}

    client.get('/repos/sinatra/sinatra')
    # => {"repo"=>#<Travis::Client::Repository: sinatra/sinatra>}
    ```
```

Becomes:

![Generated result](docs/images/img1.png)

To customize the tab label, add the `fct_label` option to your code block.

```md
    ```swift fct_label="Swift 2"
    array.enumerate()
    ```

    ```swift fct_label="Swift 3"
    array.enumerated()
    ```
```

![Generated result](docs/images/img2.png)

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

![True single_block_as_tab](docs/images/img3.png)

`single_block_as_tab: False` generates:

![False single_block_as_tab](docs/images/img4.png)

## Author 
[Yassir Barchi](http://yassir.fr)

## License

**markdown-fenced-code-tabs** is available under the MIT license. See the LICENSE file for more info.
