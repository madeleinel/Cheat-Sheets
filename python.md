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

### Getting data from the command line: raw_input (ex11)
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

## Importing modules
Importing only what the program needs helps keep the program small, and is useful for other developers to quickly gain an overview over what has been used within the code (the list of imports acts as documentation).

### Importing modules: argv (ex13)
The argument variable; holds the arguments passed to the Python script when calling it in the command line.  
Assigning "argv" to variables "unpacks" these values and make the easier to work with (like saying "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order.")  
When running these scripts, they need to be run with command line arguments.  
Eg:
```
from sys import argv
script, argument = argv
print "The script is called", script
print "This is the argument:", argument

<!-- Passing the following in the command line (note that it's including command line arguments, rather than just running "python [file-name]"):

"python [file-name] [argument-value]"
will display the following within the command line:
"The script is called [file-name]
This is the argument: [argument-value]" -->
```
As with "raw_input()", "argv" will get the value as a string (even if a number is entered; so if adding two variables will concatenate them as two strings, rather than performing a mathematical operation.)

### raw_input() vs argv
The difference between "raw_input()" and "argv" has to do with where the user is required to give input.  
If giving script inputs on the command line: use "argv".  
If giving script input using the keyboard while the script is running: use "raw_input()".  
They both get the values as a string (even if a number is entered; so if adding two variables will concatenate them as two strings, rather than performing a mathematical operation.)

### Combining raw_input() and argv: Prompting and passing (ex14)
"raw_input()" and "argv" can be combined to make the output more specific. Eg:
```
from sys import argv

script, user_name = argv
prompt = "> "

print "Hi {}, this is the {} script. I'd like to ask you a few questions.".format(user_name, script)
print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Glad to hear you're using a good {} computer, {}!
""".format(computer, user_name)

<!-- If running "python [file-name] Anna", and then entering "Apple" when asked about computer type, the following will display in the command line:

"Hi Anna, this is the [file-name] script. I'd like to ask you a few questions.
What kind of computer do you have?
> Apple
Glad to hear you're using a good Apple computer, Anna!" -->
```
Setting "prompt" to "> " will indicate where input should be provided by displaying "> " on that line.

## Functions
Create functions in Python by using "def".  
Functions in Python don't using closing brackets or anything similar; instead, it uses indentation to indicate whether the function is open or closed (ie the function is closed by going to back to not indenting the code (ie "dedenting")).  
Eg the following functions will print "Hi there!" and "Hello there Anna!" in the command line:
```
def hi():
  print "Hi there!"

def hello(name):
  print "Hello there " + name + "!"

hi()
hello("Anna")

<!-- Note that: hi() takes no argument, and hello() does -->
```

### Functions and variables
Variables can be passed into functions in several different ways.  
Eg for the function "example":
```
def example(arg1, arg2):
  print "arg1 is {}".format(arg1)
  print "arg2 is {}".format(arg2)
```
It can be called by passing the arguments directly into the function:
```
example("Hello", "Hello again")

<!-- Will print:
"arg1 is Hello
arg2 is Hello again" -->
```
It can be called by calling on variables containing the values:
```
argument_1 = "Hi"
argument_2 = "Hi again"

example(argument_1, argument_2)

<!-- Will print:
"arg1 is Hi
arg2 is Hi again" -->
```
If passing it integers, we can both use mathematical operators, and combine variables and mathematical operators. Eg:
```
example(1+2, 3+4)

<!-- Will print:
"arg1 is 3
arg2 is 7" -->

argument1 = 5
argument2 = 6

example(argument1 + 2, argument2 + 4)

<!-- Will print:
"arg1 is 7
arg2 is 10" -->
```

### Using functions to return a value
Use "return" to make a function return something / set a variable to be a value from a function.  
Eg:
```
def add(a, b):
  return a + b

<!-- the function "add" returns "a+b" > this can then be assigned to a variable, eg the variable "result" -->

result = add(3, 4)

print result

<!-- Will display "7" within the terminal -->
```
The return value of one function can also be used as an argument in another function. Chaining functions like this can be used "to create a formula using the functions." Eg:
```
def add(a, b):
    return a + b

age = add(3, 4)
<!-- age = 7 -->

def subtract(c, d):
    return c - d

example = add(age, subtract(6, 2))
<!-- ie example = add(7, (6-2)) = add(7, 4) = (7 + 4) = 11 -->

print example
<!-- Will display "11" -->
```
