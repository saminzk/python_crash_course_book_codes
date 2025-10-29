class Car():
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
    
my_new_car = Car('Toyota','Corolla A2','2008')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(20)
my_new_car.read_odometer()
my_new_car.update_odometer(10)
my_new_car.read_odometer()