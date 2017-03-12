#### Different ways of including variables within strings ####

# from Learn Python the hard way

name = "Paul"
print "let's talk about %s" % name

eyes = 'blue'
hair = 'brown'
print "he's got %s eyes and %s hair" % (eyes, hair)

# from CFG course
## this technique seems to be preferable (although can use both)

nationality = "finnish"
print "He is {0}".format(nationality)

berry = "blueberries"
fruit = "apples"
print "he likes {0} and {1}".format(berry, fruit)
print "everyone likes {} and {}".format(berry, fruit)

## if put integer within the curly brackets - {x} - then can 'reuse' the variables
print "he likes {0}, {1}, mushy {0} and red {1}".format(berry, fruit)

## to avoid depending on the .format(variables) being in the right order; could also print it as
print "he likes {berry}, {fruit} and red {fruit}".format(fruit = fruit, berry = berry)





#### More basic stuff from the session tutorial ####

print 'hello world'
print "hello" + " 5"
print "ello" * (6 / 2)
print 5**5
print "hello".upper(), "GOODBYE".lower(), "hello GoOdByE".title()
print "hello " + "world"

car = 4
driver = 2
total_drivers = car * driver
print total_drivers

a = "sarah"
f = "hello {}".format(a)
print f
a = "dave"
f = "hello {}".format(a)
print f
print f * 5

x = 1.1
x = (2 + 5 * x - x**2) / 5
print x
