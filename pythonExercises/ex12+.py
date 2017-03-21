# Ex13:
#
# from sys import argv
#
# script, first, second, third = argv
#
# print "script called", script
# print "first variable called", first
# print "second variable called", second
# print "third variable called", third
#
# ------------
#
# Ex14:
#
# from sys import argv
#
# script, user_name = argv
# prompt = "> "
#
# print "Hi {}, this is the {} script. I'd like to ask you a few questions".format(user_name, script)
# print "What kind of computer do you have?"
# computer = raw_input(prompt)
#
# print """
# Glad to hear you're using a good {} computer, {}!
# """.format(computer, user_name)
#
# ------------
#
# Ex18:
#
# def print_two(*args):
#     arg1, arg2 = args
#     print "arg1 is {}, arg2 is {}".format(arg1, arg2)
#
# def print_two_again(arg1, arg2):
#     print "and again: arg1 is {}, arg2 is {}".format(arg1, arg2)
#
# def print_one(arg):
#     print "The arg is {}".format(arg)
#
# def print_none():
#     print "There is no argument here"
#
# print_two("one", "two")
# print_two_again("ONE", "TWO")
# print_one("only one")
# print_none()
#
# ------------
#
# Ex19:
#
# def example(arg1, arg2):
#   print "arg1 is {}".format(arg1)
#   print "arg2 is {}".format(arg2)
#
# example("Hello", "Hello again")
#
# argument_1 = "Hi"
# argument_2 = "Hi again"
#
# example(argument_1, argument_2)
#
# example(1+2, 3+4)
#
# argument1 = 5
# argument2 = 6
#
# example(argument1 + 2, argument2 + 4)
#
# ------------
#
# Ex21:
#
# def add(a, b):
#     return a + b
#
# age = add(3, 4)
#
# # print add
# print age
#
# def subtract(c, d):
#     return c - d
#
# height = subtract(6, 3)
#
# # print subtract
# print height
#
# what = add(age, subtract(3, 4))
#
# print what
#
# ------------
#
# Ex__:
