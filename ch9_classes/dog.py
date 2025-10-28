class Dog():
    """"A simple class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title()+" is now rolled over.")


my_dog = Dog('buddy',3)
my_dog_2 = Dog('willie', 6)

# print(my_dog.name)
# print(my_dog.age)
print("My dog's name is "+ my_dog_2.name.title()+".")
print("My dog is "+str(my_dog_2.age)+" years old.")
my_dog_2.sit()
my_dog_2.roll_over()