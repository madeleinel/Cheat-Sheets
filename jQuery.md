# jQuery

## Introduction
A JavaScript library.  
Either download the library and link to it, or link to it from a Content Delivery Network (CDN) using:
```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
```
Negatives:
+ Less transferrable than JavaScript
+ Can increase page load, as library is very large, but usually only use a small part of it for each site.  
Need to link to it within the HTML document, at the end of the body tag (so same as for linking to JavaScript files.)  
(Eg) Makes it easy to make JS code work in the same way in different browsers. 

## JavaScript vs jQuery
Eg to get an element:  
In JavaScript:
```
document.addEventListener("DOMContentLoaded", function makeTitleStandOut() {
  const title = document.getElementById("title");
  title.style.fontSize = "48px";

  const header = document.getElementByTagName("h1")[0];   // will only target the first h1 on the page (works for getElementByTagName and -ClassName)
                                                          // (if want to target all elements with that tag name > need to create a loop)
  header.style.color = "purple";
});
```
In jQuery:  
Using "$" > Tells the browser that you are going to use the jQuery library.
```
$(document).ready(function makeTitleStandOut() {
  $("#title").css({"font-size: 48px"});

  $("h1").addClass("purpleColor")   // will target all h1's on the page
                                    // also need to add to the CSS file: ".purpleColor { color: purple; }"
  });
```
Tell the browser to only run function "now" when everything else is ready/has loaded: (necessary to do this when linking to the JS script at the end of the body tag?)  
In JavaScript:
```
document.addEventListener("DOMContentLoaded", function now());
```
In jQuery:
```
$(document).ready(function now())
```

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
