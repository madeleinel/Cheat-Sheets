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

### Changing varibles input into a string
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
