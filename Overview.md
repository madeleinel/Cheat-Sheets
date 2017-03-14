# Overview Cheat Sheet

## Introduction to coding / General coding notes
Code & Source code > a collection of computer instructions (written using a programming language that is readable to humans)
	> Coding is “the art of speaking to computers”
	> The purpose of coding is to manipulate data
	> Code put together in an ordered fashion for a specific purpose > called a program

Programming is a subset of coding
	> Programming is the process of making a concrete solution to an abstract problem (for the computer to solve)
	> Programming languages allow us to carry out e.g. mathematical equations in a program, and not all types of programming
	are meant for that purpose
	> A programming language is one that is used to build solutions to problems

Front-End
	> The parts of websites, apps and web services that users interact with (i.e. not the stuff behind the scenes)
	> Easy to visualise. "Comes easily with practice.” A good eye for design and a interest in the user journey is useful
	> Front-end technologies are also referred to as ‘client-facing’ and ‘user-facing’ technologies

Mark-up languages (HTML) vs Stylesheets (CSS) vs Programming languages (JavaScript, Python, etc)
	> Mark-up > The structure of the page
	> The presentation & styling of the page
	> Enables the page to be dynamic, user interactivity, etc (usually without needing to reload the page)

URL
	> URLs have several different parts:
		> http : the protocol or how to fetch the information
		> www.bbc.co.uk : the host or where to fetch it from
		> /news : the path or precisely what information to fetch
	> The protocol describes how the information is transmitted
		> Can be https for secured communication, ftp for file transfer, or git
	> The host describes where the information should come from
	> The path tells that location precisely what information to send

	> URLs can also be more complicated than this > they can contain query parameters, fragments and port information

IP Address
	> The computer’s unique address
	> Used for sending requests from, and returning files to, the computer
	> "The backbone of the internet is a network of routers that are responsible for routing files from one IP address to another”
	> Every computer has an internal and public-facing IP address, for the sake of security
	> IP addresses change often, as servers are commonly switched, run in parallel, and/or are back-ups
		> The internet works on a domain name system, that matches domain names to IP addresses, as IP addresses
		change often and are difficult and tedious to remember

Servers
	> Computers which host and run the code for a website
	> Usually permanently connected to the internet

DNS
	> “Domain Name System”
	> A DNS server is "basically a massive address book of IP addresses"
	> When you type a URL into the browser > the computer performs a DNS lookup
		> DNS lookup > the computer contact a DNS server, which converts the domain name from the URL into an IP
		address for a server)
		> Once the IP address of the server has been found > the request is forwarded to the server

Static vs Dynamic sites
	> Static > all pages are pre-prepared > the server just sends the pages to the browser
	> Dynamic > pages are prepared “on the fly” > by pulling information from a database, depending on the user requested
		> Most (large) pages are dynamic
		> There are many options for building dynamic server-side sites, e.g. Ruby on Rails, PHP, Django, node.js (and 			WordPress)

Publishing websites
	> Need 2 things to publish websites under your own domain name:
A web server (to serve the site)
A domain name (to point towards the site)
	> The web server doesn’t have to be physical or your own > can also use companies offering web hosting (providing space	on a shared server) > e.g. Github / Github Pages
	> Need to use a domain registrar to buy a domain name > e.g. one.com, namecheap.com
		> Domain names are separate from the hosting > don’t need to get them both through the same company

Good code
	> Nest start and closing tags properly
	> Indent the code

HTML DOM
	> HTML Document Object Model
	> Specifies the hierarchical layout of the HTML document
	> An agreed interface that is platform independent, language independent, and interacts with any markup document (e.g. HTML or XML)
	> Represents the document/site as a node tree > each node represents a part of the document (so it tells the browser where to look for a specific thing within the document)
	> Very useful for software development, using e.g. JavaScript

## Terms
(Development concepts)

### Frameworks
A framework is a platform for developing software applications; it provides a foundation on which you can build programs for a specific platform; it serves as a foundation for programming.  
Web application frameworks are designed to support the development of dynamic websites and applications.  
It helps streamline the development process, as it means you don't need to "reinvent the wheel" each time you develop a new application. It lets you benefit from peer-reviewed, tested and pre-written functionalities, which saves time and hassle.  
It may include predefined classes and functions, that can be used to process input, manage hardware devices and interact with system software.  
A frameworks includes an API, and may also include code libraries, a compiler, and other programs used in the software development process.  
It contains common code which provides generic functionality, which can be selectively overridden or specialised by user code to provide specific functionality (extensibility.)  
"A special type of software libraries; frameworks are reusable abstractions of code wrapped in a well-defined API."

### APIs
Application Programming Interface.  
An API is a set of commands, functions, protocols of objects that you can use to create software or interact with an external system.  
It provides developers with standard commands for performing common operations, so that they don't have to write the code from scratch.  
Website APIs are typically more basic (than operating system APIs), and usually allow developers to access specific information from their site; it may be only a set of XML elements and some basic commands for retrieving the information.

### Libraries
A library is an implementation of an API; it's a suite of data and programming code that is used to develop programs and applications. It assists the programmer and the compiler in building and executing software.  
It generally consists of prewritten code, classes, procedures, scripts, configuration data (and more) that developers can call upon.  
It can be manually added to a program to achieve more functionality, or to automate a process (without writing code for it.) Eg, if developing a mathematical application, adding a mathematical software library will eliminate the need for writing complex functions, as the functions within the software library can be called upon/used within the program.

### Toolkits
Toolkits are sets of libraries (APIs) and services grouped together; they provide a developers with a wider range of possible solutions, and are used to develop and maintain applications and databases.  
A toolkit can be a single utility program, a set of software routines, or a complete integrated set of software utilities.  
There are toolkits for developing almost anything.

## Languages

### JavaScript

#### Node.js
Web development framework written in Javascript.

#### jQuery
A JavaScript library.  
Need to link to it within the HTML document, at the end of the body tag (so same as for linking to JavaScript files.)  
(Eg) Makes it easy to make JS code work in the same way in different browsers.  
Eg to get an element:  
In JavaScript:
```
document.addEventListener("DOMContentLoaded", function makeTitleStandOut() {
  const title = document.getElementById("title");
  title.style.fontSize = "48px";

  const header = document.getElementByTagName("h1")[0];   // will only target the first h1 on the page
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

### Angular.js

### Python

#### Django
Web development framework written in Python.

### Ruby

#### Ruby on Rails
Web development framework written in Ruby.

## APIs

### Twitter API

## Bootstrap

### Twitter Bootstrap
[The Twitter Bootstrap](http://getbootstrap.com/) is a web application framework.  
It promotes a mobile-first approach to designing websites, encouraging you to design the site so that it looks good on all screen sizes from the beginning. It is built on a grid system consisting of 12 columns, and lets you customise the size of the HTML elements as a fraction of 12. The grid system is 'responsive, mobile-first and fluid.'  
It is used by [linking to the bootstrap stylesheet in the HTML document head tag](http://getbootstrap.com/getting-started/#download-cdn) (can be done with or without downloading Bootstrap), and [adding the relevant attributes to the HTML elements](http://getbootstrap.com/css/).  
Using it makes it easier to create responsive and cross-browser-friendly websites. It can also be used to easily get an [HTML starter template](http://getbootstrap.com/examples/starter-template/) and [add site components](http://getbootstrap.com/components/), eg responsive nav bars.  
Eg:
+ Use ".container" to center the element and provide it with sensible page margins
+ Create a column layout by using ".col-sm-4" or ".col-md-6" etc
  + col > specifies it should be a column in the grid system
  + sm & md > specifies at which screen width the class should be implemented
  + 4 & 6 > specifies how many of the 12 columns should be taken up by the element

## Testing Frameworks

### Jasmine

### Jingr (?)
