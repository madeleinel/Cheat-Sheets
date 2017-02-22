name = 'Zed A Shaw'
age = 35
height = 74
height_in_cm = height * 2.54
weight = 180
weight_in_kg = weight * 0.453592
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print "let's talk about %s" % name
print "he's %d cm tall" % height_in_cm
print "he's %r kg heavy" % weight_in_kg
print "actually that's not too heavy"
print "he's got %r eyes and %r hair" % (eyes, hair)
print "his teeth are usually %s depending on the coffee" % teeth

print "if I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)
