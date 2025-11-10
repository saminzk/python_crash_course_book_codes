#importing class from the car module file 
from car import Car

my_new_car = Car('audi','a4',2019)

print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 25
my_new_car.read_odometer()