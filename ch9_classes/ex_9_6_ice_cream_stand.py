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



class IceCreamStand(Restaurant):
    def __init__(self, flavors,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def get_available_flavors(self):
        for flavor in self.flavors:
            print(f"{flavor.title()}")
    

ice_cream_stand_1 = IceCreamStand(['Vanilla','Strawberry','Chocolate','Mango','Butterscotch'],'Doyel','mexican')
ice_cream_stand_1.get_available_flavors()




# restaurant_1 = Restaurant('Delaware','italian')