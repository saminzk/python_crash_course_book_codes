class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant's name is "+self.restaurant_name.title())
        print("This restaurant specializes in authentic "+self.cuisine_type.title()+" cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name.title()+" is now open.")