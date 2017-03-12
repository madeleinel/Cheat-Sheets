# FizzBuzz Python challenge
# (See email from Andreas from 22 Feb)

def FizzBuzz(n):
    # if/else statement
    for i in range(1, n+1):

        div_by_3 = i % 3 == 0
        div_by_5 = i % 5 == 0

        if div_by_3 and div_by_5:
            print 'FizzBuzz'
        elif div_by_3:
            print 'Fizz'
        elif div_by_5:
            print 'Buzz'
        else:
            print i

# FizzBuzz(32);

# -------- -------- -------- -------- #

### Lists & For loops & While loops & functions

# Lists
# Python lists are 0-indexed
item_list = ['item1', 'item2', 'item3']
animals = ['bear', 'horse', 'otter']
empty_list_to_fill = []

# For loops
# See Python the hard way ex32

# While loops
# See Python the hard way ex33
### Shouldn't use while loops (can easily create infinite loops)
### >> Use for loops instead

# Functions
# If don't 'return' the final variable/value within the function, it will not be available outside of that function
# >> but if you do 'return' it; can call it within other functions
### same as in JS >> 'return' exits the function

def add(num1, num2):
    result = num1 + num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

product1 = add(1,1)
product2 = add(4,5)

final_product = multiply(product1, product2)

# print product1
# print product2
# print final_product

# -------- -------- -------- -------- #

### Flask
# Lets you run web server locally, which can run inifinitely(?)
# See 'flaskApp/FlaskExs.py' for code

### GET & POST requests
# See 'contact.html' and 'FlaskExs.py' for code
