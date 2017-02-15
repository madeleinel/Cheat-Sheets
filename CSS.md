# CSS Cheat Sheet

Should (pretty much always) link to separate CSS files. That way you:
* Reduce repetition in your code and
* Reduce the amount of information that has to be sent to the browser for each page - if the CSS file applies to the whole site, it only needs to be sent to the visitor once.

## Basic Terms
```
selector {
    property: value;
}
```

```
selector {
  declaration
}
```
>> if more than one declaration >> called 'declaration block'

## Selectors

certain selectors will "override" others if they have a greater specificity value. ul li p { is more specific CSS than just p {, so when CSS sees tags that are both <p> tags and happen to be inside unordered lists, it will apply the more specific styling (ul li p {) to the text inside the lists.

There are two selectors that are even more specific than nested selectors like the ones above: classes and IDs. Check them out in the editor to the right.

### *
The universal selector; can use this to apply CSS styling to every element on the page.  
For setting background colour etc >> "better to use the body tag". For putting WIP borders around all elements within the page >> useful to use the universal selector.  
Eg:
```
* {
    border: 2px solid black;
}
```
Creates a two-pixel wide solid black border around every element on the HTML page.

### Selectors within Selectors

```
section div p { /* Some CSS */ }
```
For targetting a child on another element.  
Targets 'p' that is nested _somewhere_ inside a 'div' that's nested _somewhere_ inside a 'section'

```
div > p { /* Some CSS */ }
```
For targetting direct children of an element.  
Targets 'p' that is nested _directly_ inside of a 'div'.

### Pseudo-class selectors

```
selector:pseudo-class_selector {
    property: value;
}
```
A pseudo-class selector is a way of accessing HTML items that aren't part of the document tree (remember the tree structure we talked about earlier?). For instance, it's very easy to see where a link is in the tree. But where would you find information about whether a link had been clicked on or not? It isn't there!

Pseudo-class selectors let us style these kinds of changes in our HTML document. For example, we saw we could change a link's text-decoration property to make it something other than blue and underlined. Using pseudo selectors, you can control the appearance of unvisited and visited links—even links the user is hovering over but hasn't clicked!

Eg:  
To style a you're hovering your mouse over:
```
a:hover {
  color: purple;
}
```

To style an unvisited link:
```
a:link {
  color: blue;
}
```

To style a visited link:
```
a:visited {
  color: green;
}
```

To style only the first child(ren) of a parent(s):
```
p:first-child {
  color: yellow;
}
```

To style the fifth child(ren) of a parent(s):
```
p:nth-child(5) {
  color: orange;
}
```

When:
```
<body>
  <h3>Header</h3>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
  <p>Paragraph 3</p>
</body>
```

'Paragraph 3' is within the third paragraph, but the fourth child of the 'body', so to target it within CSS we need to use:
```
p:nth-child(4) {
    color: red;
}
```

## Measurement Units

### px
A pixel is a dot on your computer screen. Specifying font sizes in pixels is great when you want the user to see exactly on their screen what you designed on yours, though it assumes your screens are of similar size.

### em
The font-size unit em is a relative measure: one em is equal to the default font size on whatever screen the user is using. That makes it great for smartphone screens, since it doesn't try to tell the smartphone exactly how big to make a font: it just says, "Hey, 1em is the font size that you normally use, so 2em is twice as big and 0.5em is half that size!

## Positioning Properties

### Display

#### block (default):
This makes the element a block box. It won't let anything sit next to it on the page! It takes up the full width. Any element that comes in as a block (say, a paragraph) will automatically take up the full width of the page, no matter how much or how little content you put in.  
####inline-block:
This makes the element a block box, but will allow other elements to sit next to it on the same line. The blocks are still blocks, but will be able to sit next to each other on the same line. The inline-block value allows you to put several block elements on the same line.  
#### inline:
This makes the element sit on the same line as another element, but without formatting it like a block. It only takes up as much width as it needs (not the whole line). The inline value places all your elements next to one another, but not as blocks: they don't keep their dimensions. The good news is, inline places all your elements on a single line. The bad news is that it doesn't maintain their "box"ness. The inline display value is better suited for HTML elements that are blocks by default, such as headers and paragraphs.  
#### none:
This makes the element and its content disappear from the page entirely! As you might expect, this prevents the page from displaying the selected element. As you might not expect, this removes the selected element from the page entirely, including any children and any content. Poof! Gone! (But not gone forever—changing the display value away from none will bring everything back.)

### Position

#### static (deafult):
This just means "where the element would normally go." If you don't tell an element how to position itself, it just plunks itself down in the document.
#### absolute:
When an element is set to position: absolute, it's then positioned in relation to the first parent element it has that doesn't have position: static. If there's no such element, the element with position: absolute gets positioned relative to <html>.
So if:
```
<div id="outer"><div id="inner"></div></div>
#outer {
  position: absolute;
}
```
Then when positioning the '#inner' div, it will be relative to the '#outer' div.
If:
```
<div id="outer"><div id="inner"></div></div>
#outer {
  position: static;
}
```
Then the positioning of the '#inner' div would be relative to <html> (the entire HTML document).
#### relative:
This tells the element to move relative to where it would have landed if it just had the default static positioning.  
If you give an element relative positioning and tell it to have a margin-top of 10px, it doesn't move down ten pixels from any particular thing—it moves down ten pixels from where it otherwise would have been.
#### fixed:
This anchors an element to the browser window—you can think of it as gluing the element to the screen. If you scroll up and down, the fixed element stays put even as other elements scroll past.

### Float

When mixing large floating elements with non-floating ones elements can end up on top of each other.  
If you tell an element to clear: left, it will immediately move below any floating elements on the left side of the page; it can also clear elements on the right. If you tell it to clear: both, it will get out of the way of elements floating on the left and right!

  .  
to display list horisontally
>> display: inline;

to display list vertically (as default)
>> display: block;

## to make content responsive for different sized screens:

to center div
>> margin: 0 auto; // margin: auto; >> sets left/right margins to 'auto', making both of these margins stretch to the edge of the page >> centers the div
>> Setting a div's margin to auto tells the document to automatically put equal left and right margins on our element, centering it on the page.

set div 'max-width' rather than 'width'

@media (max-width: 500px) {
  body {
    font-size: 12px;
  }
}
>> set media query to activate when the devices has a max width of 500px (ie, the screen is smaller than that)



jQuery alert when click on like button:

<body>
  <button>Like</button>
</body>

<script>
  $("button").on("click", function() {
      alert("clicked!")
      });
</script>

>> $("element").on("event-type", thing-to-be-done);
>>>> the '.on()' sets up an event listener for the element
