## Upgrading

To upgrade Code Tabs to the latest version, use `pip`:

``` sh
pip install --upgrade markdown-fenced-code-tabs
```

To inspect the currently installed version, use the following command:

``` sh
pip show markdown-fenced-code-tabs
```

### Code Tabs 0.x to 1.x

* The 0.x generates exclusively a **Bootstrap 3** based template. Starting from the 1.x, you can [choose the rendering template](templates.md).

To keep everything working smoothly, you need to choose the `bootstrap3` template: 

``` yaml
markdown_extensions:
  - markdown_fenced_code_tabs:
      template: 'bootstrap3'
```

## Changelog

### 1.0.3 <small>_ May 27, 2018</small>
  * Avoid adding the `<div class="md-fenced-code-tabs"></div>` structure for single code blocks if the `single_block_as_tab` option is `True`.

### 1.0.2 <small>_ May 27, 2018</small>
  * **FIX**: Fixed the Bootsrap templates

### 1.0.1 <small>_ May 25, 2018</small>
  * **FIX**: Fixed the missing resources

### 1.0.0 <small>_ May 25, 2018</small>
  * **NEW**: Added the `active_class` option support in the configuration
  * **NEW**: Added the `template` option support in the configuration
  * **FIX**: Fixed the tab id issue for code blocks with same language #12

### 0.2.0 <small>_ June 16, 2017</small>

  * Added the custom tab label option
  * Fixed the missing `active` class of the first tab
  * Fixed the missing `string` import

### 0.1.0 <small>_ March 1, 2017</small>

  * Initial release
