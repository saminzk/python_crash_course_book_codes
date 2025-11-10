# from car import Car, ElectricCar

import car


my_beetle = car.Car('Volkswagen','beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())