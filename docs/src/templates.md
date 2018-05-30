The **Code Tabs** extension allows you to choose one of the following three rendering templates.

## Default

The default template is dependency free and needs only CSS only to work fine.

### Configuration

```yaml
markdown_extensions:
  - markdown_fenced_code_tabs:
      template: 'default'
```

Here is the basic CSS that can be used.

```css
.md-fenced-code-tabs * {
    box-sizing: border-box;
}

.md-fenced-code-tabs {
    display: flex;
    position: relative;
    flex-wrap: wrap;
    width: 100%;
}

.md-fenced-code-tabs input {
    position: absolute;
    opacity: 0;
}

.md-fenced-code-tabs label {
    width: auto;
    padding: 4px;
    margin: 0 8px;
    cursor: pointer;
    color: #aaa;
}

.md-fenced-code-tabs input:checked + label {
    color: #333;
}

.md-fenced-code-tabs .code-tabpanel {
    display: none;
    width: 100%;
    margin-top: 10px;
    order: 99;
}

.md-fenced-code-tabs input:checked + label + .code-tabpanel {
    display: block;
}

.md-fenced-code-tabs pre,
.md-fenced-code-tabs .codehilite {
    width: 100%;
    margin: 0px;
}
```

!!! tip
    Take a look to the [code-tabs css](assets/css/code-tabs.css) of this current documentation :wink:

### Generated HTML

For each code block, the generated HTML code will be:

```html
<input class="code-tab"
       role="tab"
       type="radio" 
       name="${group-id}" 
       id="${group-id}-${index}_${language-1}" 
       data-lang="${language-1}" 
       aria-controls="${group-id}-${index}_${language-1}-panel">

<label class="code-tab-label"
       for="${group-id}-${index}_${language-1}" 
       data-lang="${language-1}" 
       id="${group-id}-${index}_${language-1}-label">Label 1</label>

<div class="code-tabpanel" 
     role="tabpanel" 
     data-lang="${language-1}" 
     id="${group-id}-${index}_${language-1}-panel" 
     aria-labelledby="${group-id}-${index}_${language-1}-label">Code 1</div>
```

Exemple: 

```` markdown
``` c
printf("HELLO WORLD!");
```

``` java 
System.out.println("HELLO WORLD!");
```
````

Result:

``` HTML
<div class="md-fenced-code-tabs" id="tab-tab-group-4">
    <input name="tab-group-4" type="radio" id="tab-group-4-0_c" checked="checked" class="code-tab" data-lang="c" aria-controls="tab-group-4-0_c-panel" role="tab">
    <label for="tab-group-4-0_c" class="code-tab-label" data-lang="c" id="tab-group-4-0_c-label">C</label>
    <div class="code-tabpanel" role="tabpanel" data-lang="c" id="tab-group-4-0_c-panel" aria-labelledby="tab-group-4-0_c-label">
        ... the highlighted syntax ...
    </div>
    <input name="tab-group-4" type="radio" id="tab-group-4-1_java" class="code-tab" data-lang="java" aria-controls="tab-group-4-1_java-panel" role="tab">
    <label for="tab-group-4-1_java" class="code-tab-label" data-lang="java" id="tab-group-4-1_java-label">Java</label>
    <div class="code-tabpanel" role="tabpanel" data-lang="java" id="tab-group-4-1_java-panel" aria-labelledby="tab-group-4-1_java-label">
        ... the highlighted syntax ...
    </div>
</div>
```

## Bootsrapt

If you're using a Bootstrap based theme, the only thing you'll need to is choosing the right template option depending on the Bootstrap version of you're theme.

### Bootsrapt 3

```yaml
markdown_extensions:
  - markdown_fenced_code_tabs:
      template: 'bootstrap3'
```

For the same previous exemple, the generated code will be:

``` HTML
<div class="md-fenced-code-tabs" id="tab-tab-group-4">
    <ul class="nav nav-tabs">
        <li class="nav-item active"><a href="#tab-group-4-0_python" role="tab" data-toggle="tab" data-lang="python">Python 2</a>
        </li>
        <li class="nav-item"><a href="#tab-group-4-1_python" role="tab" data-toggle="tab" data-lang="python">Python 3</a>
        </li>
    </ul>
    <div class="tab-content">
        <div id="tab-group-4-0_python" class="tab-pane active" role="tabpanel">
            ... the highlighted syntax ...
        </div>
        <div id="tab-group-4-1_python" class="tab-pane" role="tabpanel">
        ... the highlighted syntax ...
        </div>
    </div>
</div>
```

### Bootsrapt 4

```yaml
markdown_extensions:
  - markdown_fenced_code_tabs:
      template: 'bootstrap4'
```

This time the result will be:

``` HTML
<div class="md-fenced-code-tabs" id="tab-tab-group-4">
    <ul class="nav nav-tabs">
        <li class="nav-item"><a class="nav-link active" href="#tab-group-4-0_c-panel" role="tab" id="tab-group-4-0_c-tab" data-toggle="tab" data-lang="c" aria-controls="tab-group-4-0_c-panel" aria-selected="true">C</a>
        </li>
        <li class="nav-item"><a class="nav-link " href="#tab-group-4-1_java-panel" role="tab" id="tab-group-4-1_java-tab" data-toggle="tab" data-lang="java" aria-controls="tab-group-4-1_java-panel" aria-selected="false">Java</a>
        </li>
    </ul>
    <div class="tab-content">
        <div id="tab-group-4-0_c-panel" class="tab-pane show active" role="tabpanel" aria-labelledby="tab-group-4-0_c-tab">
            ... the highlighted syntax ...
        </div>
        <div id="tab-group-4-1_java-panel" class="tab-pane " role="tabpanel" aria-labelledby="tab-group-4-1_java-tab">
            ... the highlighted syntax ...
        </div>
    </div>
</div>
```
