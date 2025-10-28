class Restaurant: 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restautant(self):
        print("Restaurant's name is "+self.restaurant_name.title())
        print("This restaurant specializes in authentic "+self.cuisine_type.title()+" cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name.title()+" is now open.")



restaurant_1 = Restaurant('Delaware','italian')
restaurant_2 = Restaurant('Hashito','japanese')
restaurant_3 = Restaurant("Wang min",'chinese')


restaurant_1.describe_restautant()
restaurant_1.open_restaurant()
print('\n\n')
restaurant_2.describe_restautant()
restaurant_2.open_restaurant()
print('\n\n')