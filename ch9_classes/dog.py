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

print(my_dog.name)
print(my_dog.age)