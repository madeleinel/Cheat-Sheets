# JavaScript Cheat Sheet

##Introduction

### To run JavaScript
To tell the site to only run the function "now" when the content of the page has been loaded(?)  
(Necessary to do this when linking to the JS script at the end of the body tag?)
```
document.addEventListener("DOMContentLoaded", function now() {});
```

### Indicating JS within the HTML file
If going to target an HTML element through JavaScript, eg through its ID name, it's useful to include "js" within the ID name, to make it clearer for people reading the code that the element (& some of its styling) will be targeted/manipulated through JS.  
Eg "#js-increase-size" rather than "#increase-size".

## Basics

### Numbers

### Strings
Flat text surrounded by quotation marks.

### Concatenation
Strings can be concatenated by adding strings together. Eg:
```
"Hello " + "there!" >> "Hello there!"
```
Strings can also be concatenated with numbers and expressions. Eg:
```
"I am " + 10 + " years old" >> "I am 10 years old"
1/2 + " of the pie remains" >> "0.5 of the pie remains"
```
Note that expressions get evaluated before being entered into the string. To avoid this (eg when you want a number expressed as a fraction within the text), it must be entered as a string, eg:
```
"1/2" + " of the pie remains" >> "1/2 of the pie remains"
```

## Operators

### Comparators signs
Using these will return a Boolean (True or False).  
Case sensitive when comparing strings.

#### ==
Equal to (but not same type)
```
5 == "5"                  // will return True
"Hi there" == "Hi there"  // will return True
```

#### ===
Equal to (and same type)
```
5 === "5"  // will return False
```

#### !=
Not equal to
```
5 != 6                    // will return True
"Napoleon" != "napoleon"  // will return True (as case sensitive)
```

#### Less than or Greater then
< or > or >= or >=  
```
5 < 6                                     // will return True
2 >= 4                                    // will return False
"hi there".length > "hello there".length  // will return False  (string.length will count all characters, alphabetical and non-alphabetical)
```

### Booleans

## Special characters
(Used within strings)

### Escaping characters
Using "\" will escape characters (ie enable displaying them) that would otherwise not be interpreted as part of the string by JavaScript.

#### Quotation marks
To display quotation marks (so JavaScript doesn't think it's just marking the end and beginning of a string, and thus end the string too early):
```
"Some people say cats are \"adorable\" but I know better"
```
Will display: "Some people say cats are "adorable" but I know better"

#### Backslashes
To display backslashes:
```
"The file is in \\myDocuments\\Pictures"
```
Will display: "The file is in \myDocuments\Pictures"

### Inserting tabs, new lines, etc
The "\" followed by a character can also be used to insert tabs, new lines, etc.

#### Inserting tabs  
"\t" will insert a tab:
```
"Date:\t24\tJanuary,\t\t2017"
```
Will display: "Date: 24  January,    2017"

#### Inserting new lines
"\n" will insert a new line:
```
"Here is a list:\nItem 1\nItem 2"
```
Will display as:  
"Here is a list:  
Item 1  
Item 2"

#### Combining them
```
"Departure:\t09.00\nArrival:\t14.00"
```
Will display as:  
"Departure: 09.00  
Arrival:    14.00"

## Common Terms

### console.log();
### console.table();
### alert();
This command will open a pop-up window displaying the string you feed it.
Eg:
```
alert("it works!");
```
Will display a pop-up window reading "It works!".  
Using alert(); before adding JS will alert you to if something is not working previously >> ie if the alert window doesn't open upon loading the page >> you'll know it's not due to your code, but another issue somewhere else.

## Key Words

## Higher-Order Functions

## Regex

## Array methods

### .filter

### .map

### .sort

### .reduce











## more...

object-oriented programming
functional programming
>> JS allows you to do both

// // .filter                   // // ...all of these functions will automatically loop through all objects within the array
// // .map                      // //
// // .sort                     // //
// // .reduce                   // //
