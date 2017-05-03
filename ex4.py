# = is making names for things - tells us how many cars there are
cars = 100
# we are creating variables like space_in_a_car and setting it = equal to a floating point 4.0 - let's us know how much space is available in a car
space_in_a_car = 4.0
# tells us how many drivers there are
drivers = 30
# tell us how many passengers there are
passengers = 90
# tell us how many of the cars are not being driven by subtract the number of cars from the number of drivers
cars_not_driven = cars - drivers
# Tells us how many cars are being driven by using the drivers variable
cars_driven = drivers
# Tells us the carpool_capacity by multiplying cars_driven variable by the space_in_a_car varaible
carpool_capacity = cars_driven * space_in_a_car
# Tells us the average_passengers_per_car by dividing the passengers variable by the cars_driven variable
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
