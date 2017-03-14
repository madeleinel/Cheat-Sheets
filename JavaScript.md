# JavaScript Cheat Sheet

## To run JavaScript
To tell the site to only run the function "now" when the content of the page has been loaded(?)  
(Necessary to do this when linking to the JS script at the end of the body tag?)
```
document.addEventListener("DOMContentLoaded", function now() {});
```

## Common Terms
console.log();
console.table();

```
alert();
// OR //
alert("it works!");
```
> Using alert("hello"); before adding JS will alert you to if something is not working previously >> ie if the alert window doesn't open upon loading the page >> you'll know it's not due to your code, but another issue somewhere else

object-oriented programming
functional programming
>> JS allows you to do both

// // .filter                   // // ...all of these functions will automatically loop through all objects within the array
// // .map                      // //
// // .sort                     // //
// // .reduce                   // //


## Key Words

## Higher-Order Functions

## Regex

## Array methods

### .filter

### .map

### .sort

### .reduce

## Show or Hide image description (using jQuery)
Including 'sliding effect' defined in CSS.

### HTML
```
<body>
  <div class="menuItem">
    <p>Spaghetti Carbonara <span class="price">£14</span><br />
    <small>Spaghetti-shaped spaghetti with a meat-based carbonara sauce.</small></p>
  </div>
</body>
```

### CSS
```
.menuItem {
  height: 200px;
  background-size: cover;
  position: relative;
  background-image: url("http://dash.ga.co/assets/firstcourse.jpg");
}

p {
  color: rgba(255,255,255,1);
  background: rgb(0,0,0);
  text-align: justify;
  position: absolute;
  bottom: 0;
  margin: 0;
  height: 30px;
  transition: height .5s;
  -webkit-transition: height .5s;
  -moz-transition: height .5s;
}

small {
  opacity: 0;
}

.show-description p {
  height: 150px;
}

.show-description small {
  opacity: 1;
}
```

### JavaScript (jQuery)
```
// link to the GA jQuery library within the html <head> tag //
<script src="/assets/jquery.js"></script>

// add this code at the end of the html <body> tag //
  $('div').on('click', function() {
    $(this).toggleClass('show-description');
  });
```
