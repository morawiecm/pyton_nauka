cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("Dostepmnych jest", cars, "samochodow")
print("Dostepnych jest tylko", drivers, "kierowcow")
print("Dzis bedzie", cars_not_driven, "pustych samochodow")
print("Dzis mozemy przetransportowac", carpool_capacity, "osob")
print("Mamy dzis do przewiezienia", passengers, "pasazerow")
print("Musimy umiescic srednio", average_passengers_per_car, "osoby w aucie")
