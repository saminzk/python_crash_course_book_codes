class User:
    def __init__(self, first_name, last_name,date_of_birth,city, state, country):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.city = city
        self.state = state
        self.country = country

    def describe_user(self):
        print("Users full name is "+self.first_name.title()+" "+self.last_name.title()+".")
        print(f"{self.first_name.title()} {self.last_name.title()}'s of birth is "+self.date_of_birth)
        print(f"{self.first_name.title()} {self.last_name.title()} live is {self.city.title()}, {self.state.title()}, {self.country.title()}.") 
           
    def greet_user(self):
        print("Hello "+self.first_name.title()+" "+self.last_name.title()+".")



person_1 = User("John", "Snow", "December 26, 441", "Winterfell", 'North', 'Westeros')
person_2 = User('Mr', 'No One', 'January 1, 420','Bravos','Bravos','Essos')

person_1.describe_user()
person_1.greet_user()

person_2.describe_user()
person_2.greet_user()

