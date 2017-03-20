# Python Cheat Sheet

## Overview

### Flask
Web (micro)framework for Python.  
Based on Werkzeug and Jinja 2.

### pip
Package management system used to install and manage software packages / libraries written in Python.  
Can be used to install eg Flask.

## Data types
### String
Contains words, sentences, etc.

### Integer
Whole numbers, eg "3".

### Modulus / Remainder
Will return the remainder of a division, eg "10/3 = 3 with a remainder of 1" > "10%3 = 1".

### Float
Numbers using decimal points, eg "3.333".

## Misc useful commands

print
mathematical operators

## String methods
When a method is attached to a string, it causes Python to do the relevant processing on the string. Eg:
 + "string here".upper() > "STRING HERE"
 + "STRING HERE".lower() > "string here"
 + "string here".title() > "String Here"
 + "String Here".swapcase() > "sTRING hERE"

## Variables

### To assign variables
To assign a value to a variable, simple use:
```
variable = "value"
age = 5
his_name = "Peter"
```

### To input variables into strings
Use "{}" as placeholders for the variables within the string, and then state which variables to be used. Eg:
```
name = "Sophie"
age = 10

her_name = "Her name is {} and she is {} years old".format(name, age)

/* Note that the variables here need to be listed in the order they appear in the string */
/* Can also number the "{}", so that the variables can be reused */

her_name_again = "Her name is {0} and she is {1} years old. She prefers to be called {1}-year-old {0}".format(name, age)

/* Can also input placeholder 'variables' to call the variables within the string */

her_name_third_time = "Her name is {word} and she is {number} years old".format(word = name, number = age)

/* Can also use "% syntax" (although this is not the preferred way to print variables) */

her_name_fourth_time = "Her name is %s and she is %d years old" % (name, age)
```

### Changing varibles' input into a string
Once variables has been "baked into" a string, changing the variable won't update the string; need to restate the string to do this. Eg:
```
name = "Dave"
hello = "hello {0}".format(name)
name = "Sarah"
/* > print hello > "hello Dave" */

/* need to restate the string to update the variable within it */

hello = "hello {0}".format(name)
/* > print hello > "hello Sarah" */
```

## Input through the command line
Code that takes input from the command line and "does something with it."

### Getting data from the command line (ex11)
```
value = raw_input()
```
will assign a value entered through the command line. This will get the value as a string (even if a number is entered; so if adding two variables will concatenate them as two strings, rather than performing a mathematical operation.)  
Eg for typing the following in a python file & running it in the command line:
```
print "What's your name?",
name = raw_input()
print "My name is {}".format(name)

/* If input "Madde" on the command line > will print "My name is Madde" */
/* Adding "," at the end of the "print" line will make the "raw_input" go on the same line (rather than a new line) */

print "x should be",
x = raw_input()
print "y should be",
y = raw_input()
print (x + y)

/* If input x=2 and y=3 > will print "23" (rather than "5") */
```

### Prompts in the command line (ex12)
The prompts can also be put directly inside "raw_input", thus avoiding having to print the question before the "raw_input", eg:
```
name = raw_input("What's your name? ")
print "My name is {}".format(name)

x = raw_input("x should be ")
y = raw_input("y should be ")
print (x + y)

/* These will both display in the command line in the same way as the above examples (in "Getting data from the command line") */
```

### Prompting and passing (ex14)
