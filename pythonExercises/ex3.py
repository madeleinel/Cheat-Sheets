# * and % have the same priority,
# and associativity from left to right
##

print "I will now count my chickens:"

# Calculate 25 + (30/6) = 25 + 20 = 55
print "Hens", 25 + 30 / 6
# Calculate 100 - (75 % 4) = 100 - 3 = 97
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

# Calculate 3 + 2 + 1 - 5 + (0) - (0.25) + 6 =
# = 6 - 5 - 0.25 + 6 = 6.75
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

print "Is it true that 3 + 2 < 5 - 7?"

# check whether 5 < -2 >> this is false
print 3 + 2 < 5 -7

print "what is 3 + 2?", 3 + 2
print "what is 5 - 7?", 5 - 7

print "oh, that's why it's false"

print "how about some more"
print "is it greater?", 5 > -2
print "is it greater or equal?", 5 >= -2
print "is it less or equal?", 5 <= -2

print 7/4
print 7.0/4.0

print 3 % 4
print 25 * 3 % 4
print 75 % 4
print 3 + 2 + 1 - 5 + 4 % 2 - 1
print 4 % 2

print 11/3
print 11.0/3.0
