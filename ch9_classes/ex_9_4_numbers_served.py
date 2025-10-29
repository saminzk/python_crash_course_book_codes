class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restautant(self):
        print("Restaurant's name is "+self.restaurant_name.title())
        print("This restaurant specializes in authentic "+self.cuisine_type.title()+" cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name.title()+" is now open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self):
        self.number_served = self.number_served + 1

    def get_number_of_served(self):
        print(f"{self.restaurant_name.title()} served {self.number_served} customers total.")



restaurant_1 = Restaurant('Wang min','Chinese')

restaurant_1.open_restaurant()

restaurant_1.set_number_served(999)

restaurant_1.get_number_of_served()

restaurant_1.increment_number_served()

restaurant_1.get_number_of_served()