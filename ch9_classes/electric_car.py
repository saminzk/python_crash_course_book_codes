class Car():
#class is defined like this => class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    

    def update_odometer(self, milage):
        """Set the odometer reading to a value.
           Reject the change if it attempts to roll the odometer back.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back on odometers")
    
    def read_odometer(self):
        print("This car  has "+str(self.odometer_reading)+" miles on it.")



class ElectricCar(Car):
    def __init__(self, make, model, year):
        #in python 2.7 super is used like below
        # super(ElectricCar, self).__init__(make, model, year)
        super().__init__(make, model,year)
        self.batter_size = 70

    def describe_battery(self):
        """"Print a statement describing the battery size."""
        print("This car has a "+str(self.batter_size)+ "-kWh battery.")
    
    def fill_gas_tank(self):
        """Electric cars dont have gas tank"""
        print("This car doesn't need a gas tank.")


my_tesla = ElectricCar('Tesla','Model S',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()