# HTML Cheat Sheet

## Links

### Linking text
```
<a href="https://url.com">Description of link</a>
```

### Linking an image
```
<a href="https://url.com">
  <img src="https://url.com">
</a>
```

## Images

### Linking to an online image
```
<img src="https://url.com">   [<..."url" />]?
```

### Linking to a local image
```
<img src="">
```

## Lists

### Ordered lists
Creates a numbered list

```
<ol>
  <li>List item 1</li>
  <li>List item 2</li>
</ol>
```

### Unordered lists
Creates an bullet point list

```
<ul>
  <li>List item 1</li>
  <li>List item 2</li>
</ul>
```

### Nested lists

```
<ol>

  <li>List item 1
    <ol>
      <li>Sublist Item 1</li>
      <li>Sublist Item 2</li>
    </ol>
  </li>

  <li>List item 2
    <ol>
      <li>Sublist Item 1</li>
      <li>Sublist Item 2</li>
    </ol>
  </li>

</ol>
```

## Tables

Table tag:
```
<table>Table</table>
```

Table row tag:
```
<tr>Table Row</tr>
```

Table Data (column) tag:
```
<td>Table Data</td>
```

To create a table with three rows:
<table>Table 1
  <tr>Row 1
  </tr>
  <tr>Row 2</tr>
  <tr>Row 3</tr>
</table>
```
<table>Table 1
  <tr>Row 1</tr>
  <tr>Row 2</tr>
  <tr>Row 3</tr>
</table>
```

To set table columns; tell each row how many Table Data cells (ie how many columns) to have:
```
<table>Table 1
  <tr>Row 1
    <td>Table Data 1</td>
    <td>Table Data 2</td>
  </tr>
  <tr>Row 2
    <td>Table Data 1</td>
    <td>Table Data 2</td>
  </tr>
</table>
```
###

## Inline CSS
Allows for styling of the content through the html file

### Style attribute
This tag can be used for paragraphs, headings, links and tables (and likely more)

To set the font size of a paragraph:
<p style="font-size: 20px">Text</p>
```
<p style="font-size: 20px">Text</p>
```

To set the font colour of a heading:
<h1 style="color: black">Text</h1>
```
<h1 style="color: black">Text</h1>
```

To set the font type, background colour, border thickness and text alignment of a heading:
<h2 style="font-family: Arial; background-color: blue; border: 1px; text-align: center">Text</h2>
```
<h2 style="font-family: Arial; background-color: blue; border: 1px; text-align: center">Text</h2>
```
### Styling tags
To bold the text:
<strong>Text</strong>
```
<strong>Text</strong>
```

To italicize the text:
<em>Text</em>
```
<em>Text</em>
```
