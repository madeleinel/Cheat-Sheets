// Make the first h2 green when clicking on it

$("#makeGreen").click(function() {
  $("#makeGreen").css({"color": "lightGreen"});
});

// Create an image carousel using bxslider (http://bxslider.com/)

$(document).ready(function(){
  $('.bxslider').bxSlider();
});

// Make the second h2 disappear when hovering over it, and come back into view when stop hovering

$("#hoverDisappear").hover(function() {
  $("#hoverDisappear").fadeOut(1000);
  $("#hoverDisappear").fadeIn(1000);
});

// Make the paragraph font size larger everytime it's "touched" by the mouse (ie hovered over)

$("#biggerOnClick").hover(function() {
  var fontSize = parseInt($("#biggerOnClick").css("font-size"));
  fontSize = fontSize + 1 + "px";
  $("#biggerOnClick").css({ "font-size": fontSize});
});

// Make several actions possible for this paragraph

// Change text alignment when click on the paragraph
$("#multipleActions").click(function() {
  $("#multipleActions").css({"text-align": "center"});
});

// Change text colour when hover over the paragraph
$("#multipleActions").hover(
  // when hover in
  function() {
  $("#multipleActions").css({"color": "purple"});
  // when hover out
  }, function() {
  $("#multipleActions").css({"color": "black"});
  }
);

// When click on the button, animate the text in the following div

$("#clickBtn").click(function() {
  $("#animated").animate({
    height: "+=150px",
    width: "+=150px",
  });
});
