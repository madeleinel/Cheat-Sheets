cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

# set cars_not_driven to be cars (100) - drivers (30)
cars_not_driven = cars - drivers
cars_driven = drivers
# set carpool_capacity to cars_driven (= drivers = 30) * space_in_a_car (4)
carpool_capacity = cars_driven * space_in_a_car
# set average_passengers_per_car to passengers (90) / cars_driven (= drivers = 30)
average_passengers_per_car = passengers / cars_driven

print "there are", cars, "cars available"
print "there are only", drivers, "drivers available"
print "there will be", cars_not_driven, "empty cars today"
print "we can transport", carpool_capacity, "people today"
print "we have", passengers, "to carpool today"
print "we need to put about", average_passengers_per_car, "in each car"
