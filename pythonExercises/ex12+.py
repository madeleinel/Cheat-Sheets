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
# Ex29:
#
# ten = 10
# twenty = 20
# thirty = 30
#
# if ten > twenty:
#     print "ten is greater than twenty"
#
# if ten < twenty:
#     print "twenty is greater than ten"
#
# thirty += 5
#
# print "thirty is now 35"
# print thirty
#
# if thirty >= twenty:
#     print "35 is greater than or equal to 20"
#
# if twenty <= ten:
#     print "20 is lesser than or equal to 10"
#
# ------------
#
# Ex30:
#
# ten = 10
# twenty = 20
#
# if ten > twenty:
#     print "ten is greater than twenty"
# elif ten < twenty:
#     print "twenty is greater than ten"
# else:
#     print "the two integers can't be compared"
#
# ------------
#
# Ex31:
#
# print "you are presented with a narrow path and a wide path. Which one do you choose?"
# path = raw_input("> ")
#
# if path == "narrow":
#     print "the path seems a bit narrow for your canoe. You can choose to either swim or take the canoe. Which do you choose?"
#     print "1. Swim"
#     print "2. Take the canoe"
#     transport = raw_input("> ")
#
#     if transport == "1":
#         print "good choice; you swim down the path to the beach"
#     elif transport == "2":
#         print "the path is too narrow to navigate the canoe; you get stuck"
#     else:
#         print "that was not one of the options..."
#
# if path == "wide":
#     print "good choice: now you can stay dry in your canoe"
