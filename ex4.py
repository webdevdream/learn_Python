cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Available cars
print ("There are", cars, "cars available.")
# Available drivers
print ("there are only", drivers, "drivers available.")
# Empty Cars
print ("There will be", cars_not_driven, "empty cars today.")
# How many we can transport
print ("We can transport", carpool_capacity, "people today.")
# passengers count
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.") # passengers per car
