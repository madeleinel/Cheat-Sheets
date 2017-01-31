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
Creates a bullet point list

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

### Table tags
_Table set-up_  

  Table tag:
```
<table>Table</table>
```

Table head tag:  
Contains heading information (the row/column headers) about the table.
```
<thead>Table Head</thead>
```

Table body tag:  
Contains the tabular data (the table cells) of the table.
```
<tbody>Table Body</tbody>
```

_Table content_  

  Table row tag:  
Each tag contains one row of the table.
```
<tr>Table Row</tr>
```

Table data (column) tag:  
Each tag contains one column within the current row.
```
<td>Table Data</td>
```

Table header tag:
```
<th>Table Header</th>
```

### Creating tables

_Table rows_  

  To create a table with three rows:
```
<table>
  <tr>Row 1</tr>
  <tr>Row 2</tr>
  <tr>Row 3</tr>
</table>
```

_Table columns_  

  To set table columns; tell each row how many Table Data cells (ie how many columns) to have.  

To create a table with two rows and two columns:
```
<table>
  <tr>
    <td>Table Data 1</td>
    <td>Table Data 2</td>
  </tr>
  <tr>
    <td>Table Data 3</td>
    <td>Table Data 4</td>
  </tr>
</table>
```

_Table headers_  

  To create a table with three rows, two columns and two column headers:
```
<table>
  <thead>
    <tr>
      <th>Column Header 1</th>
      <th>Column Header 2</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Row 1, Column 1</td>
      <td>Row 1, Column 2</td>
    </tr>
    <tr>
      <td>Row 2, Column 1</td>
      <td>Row 2, Column 2</td>
    </tr>
    <tr>
      <td>Row 3, Column 1</td>
      <td>Row 3, Column 2</td>
    </tr>
  </tbody>
</table>
```

_Table title_  

  To create a table with two rows, three columns, three column headers and a title spanning all three columns:
```
<table>
  <thead>
    <tr>
      <th colspan="3">Table Title</th>
    </tr>
    <tr>
      <th>Column Header 1</th>
      <th>Column Header 2</th>
      <th>Column Header 3</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Row 1, Column 1</td>
      <td>Row 1, Column 2</td>
      <td>Row 1, Column 3</td>
    </tr>
    <tr>
      <td>Row 2, Column 1</td>
      <td>Row 2, Column 2</td>
      <td>Row 2, Column 3</td>
    </tr>
  </tbody>
</table>
```

### Table styling
Colspan attribute:  
By default, each table cell takes up one column. Use the colspan attribute to define how many columns a cell should take up.
```
<th colspan="4">This cell will take up four columns</th>
```

Borders:  
To set a 1px border around the entire table and each cell, set a border within the table tag:
```
<table border="1px">
  Table content
</table>
```

Styling attributes:  
Same as with non-table tags, table tags can be styled in HTML using style attributes.
To create a table with two rows and two columns, blue text on the first row and green text on the second row:
```
<table>
  <tr style="color: blue">
    <td>Table Data 1</td>
    <td>Table Data 2</td>
  </tr>
  <tr style="color: green">
    <td>Table Data 3</td>
    <td>Table Data 4</td>
  </tr>
</table>
```

To create a table with two rows and two columns, and a border between each cell (ie between the two rows, and the two columns):
```
<table style="border-collapse: collapse">
  <tr style="border-bottom: 1px solid black">
    <td>Table Data 1</td>
    <td style="border-left: 1px solid black">Table Data 2</td>
  </tr>
  <tr>
    <td>Table Data 3</td>
    <td style="border-left: 1px solid black">Table Data 4</td>
  </tr>
</table>
```

## Inline CSS
Allows for styling of the content through the html file

### Style attribute
This tag can be used for paragraphs, headings, links and tables (and likely more)  

To set the font size of a paragraph:
```
<p style="font-size: 20px">Text</p>
```

To set the font colour of a heading:
```
<h1 style="color: black">Text</h1>
```

To set the font type, background colour, border thickness and text alignment of a table:
```
<table style="font-family: Arial; background-color: blue; border: 1px; text-align: center">Text</table>
```
### Styling tags
To bold the text:
```
<strong>Text</strong>
```

To italicize the text:
```
<em>Text</em>
```
