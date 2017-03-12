######## CALLING VARIABLES ########

my_name = "Anna"

print "Hello {name}!".format(name = my_name)

# OR
# print "Hello {0}!".format(my_name)
# OR
# print "Hello {}!".format(my_name)
# OR
# print "Hello %s!" % my_name
#
#### BUT the first method is more clear (& then the second method)
#### >> esp when inserting several variables into the same string

######## CALLING ON PARTS OF VARIABLES ########

# Can call on specific characters within a string or number
# See ex11 & E's link

######## FUNCTIONS ########

# to define a function: 'def + [function-name]():
# [tell the function what to do]'

def say_hello():
    print "Hello"

say_hello()

#### INDENTATION is really important in Python
#### >> as eg functions are not closed using parenthese, curly brackets, etc
#### >>>> Python will know whether the funciton is still open, or closed, based on the level of indentation you're on
#### eg: 'print: "haha"' is defined outside of the 'say_goodbye' function
#### >> the 'say_goodbye' function needs to be called in order to be printed; 'print: "haha"' will print regardless of the function being called

def say_goodbye(name):
    print "goodbye", name

print "haha"

say_goodbye("Anton")
# OR
say_goodbye(name = "Anton")

# ---------------- #

######## Learn python the hard way - Sessions 11-34 ########

# Ex11
# use 'raw_input' to let the user enter values through the terminal, to then be called on within the string on line 28
# put a comma behind each print statement to insert the value on the same line as the question; if remove commas, new values will be input on a new line, underneath the question line

# print "how old are you?",
# age = raw_input()
# print "how tall are you?",
# height = raw_input()
# print "how much do you weigh?",
# weight = raw_input()
# print "so you're %r old, %r tall and %r heavy" % (age, height, weight)

print "what is your spirit animal?",
spirit_animal = raw_input()
print "what is your favorite colour?",
fave_color = raw_input()
print "where are you from?",
lang = raw_input()
print "Your super secret spy name is {0:.3} {1} {2}".format(lang, fave_color, spirit_animal)

# Ex12

age = raw_input("how old are you? ")
height = raw_input("how tall are you? ")
weight = raw_input("how much do you weigh? ")

print "so you're %r old, %r tall and %r heavy" % (age, height, weight)

# Ex13 (WIP)

# from sys import argv
#
# script, first, second, third = argv

# Ex14 (WIP)
# 'argv' allows us to define a value within the terminal (?)

from sys import argv

script, name = argv

print "Hi, I'm {name}".format(name = name)

# Running 'python ex2.py [name]' within the terminal >> will print "Hi, I'm [name]" within the terminal
# If run 'python ex2.py' >> won't work, as then there will be no defined name to call on

# Ex18

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing"

print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("first")
print_none()

# Ex21




# Logic exercise
#### Booleans (True , False
)
#### When need to fulfill true/false criteria to run or not run / be true or false
#
# True OR False = True
# Have apple OR Don't have apple >> having apple trumps = True
# Can only get into restaurant if you have reservation OR in group of >4 >> only 1 needs to be true for entry to the restaurant
#
# True AND False = False
# Have apple AND don't have apple >> not having apple trumps = False
# Can only get into restaurant if you have reservation AND in group of >4 >> need both to be true for entry to the restaurant
