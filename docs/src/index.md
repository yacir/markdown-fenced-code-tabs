# Code Tabs Extension <small>Documentation</small>

!!! important ""
    Migrating from an older version? Check out our [Release notes](release-notes.md).

## Overview

**Code Tabs** is an extension that generates a HTML structure for consecutive fenced code blocks content. It provides four features:

- [X] The ability to choose the HTML template.
- [X] The ability to specify custom label for a tab.
- [X] The ability to enable tab generation for a single fenced code block.
- [X] The ability to specify the css class for the tab active state.

Example:

```` markdown
``` c
printf("HELLO WORLD!");
```

``` java 
System.out.println("HELLO WORLD!");
```

``` python
print("HELLO WORLD!")
```
````

Result:

``` c
printf("HELLO WORLD!");
```

``` java 
System.out.println("HELLO WORLD!");
```

``` python
print("HELLO WORLD!")
```

## Installation

Installation is easy with pip:

``` sh
pip install markdown-fenced-code-tabs
``` 

If you want to manually install it, run `python setup.py build` and `python setup.py install`. You should be able to access the extensions in Python Markdown.

If you would like to modify the code, you can install it via: `python setup.py develop`. This method will allow you to instantly see your changes without reinstalling.

## Usage 

In order to enable the extension just add it to your **markdown_extensions** list:

``` yaml
markdown_extensions:
  - markdown_fenced_code_tabs
```

This will add the extension with the default [options](#options). To configure them: 

``` yaml
markdown_extensions:
  - markdown_fenced_code_tabs:
      single_block_as_tab: False
      active_class: 'active'
      template: 'default'
```

!!! important
    If you choose the `default` template you wiLl have to add the needed **css** as explained in the [templates documentation](templates.md). 
    
### Label customization

By default the tab label is the language of the code block but it can be customized by passing the title to the `fct_label` argument placed right after the language identifier.

Example:

```` markdown
``` python fct_label="Python 2"
print "Bonjour" 
```

``` python fct_label="Python 3"
print("Bonjour")
```
````

Result:

``` python fct_label="Python 2"
print "Bonjour" 
```

``` python fct_label="Python 3"
print("Bonjour")
```

## Options

The following options are provided to configure the output:

Option                         | Type | Default | Description
------------------------------ | -----| --------| -----------
`single_block_as_tab`          | bool | `False` | Renders a single fenced code block as a tab.
`active_class`                 | string | `active` | Class name is applied to the active tab. 
`template`                     | string | `default`| A string that specifies which HTML template should be used `default`, `bootstrap3`, or `bootstrap4`.