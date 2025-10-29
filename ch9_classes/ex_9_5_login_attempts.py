class User():
    def __init__(self, first_name, last_name,date_of_birth,city, state, country):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.city = city
        self.state = state
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print("Users full name is "+self.first_name.title()+" "+self.last_name.title()+".")
        print(f"{self.first_name.title()} {self.last_name.title()}'s of birth is "+self.date_of_birth)
        print(f"{self.first_name.title()} {self.last_name.title()} live is {self.city.title()}, {self.state.title()}, {self.country.title()}.") 
           
    def greet_user(self):
        print("Hello "+self.first_name.title()+" "+self.last_name.title()+".")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts
    

user_1 = User('Samin','Khan','21-Nov-1998' ,'Dhaka', 'Dhaka','Bangladesh')

user_1.describe_user()

print(user_1.increment_login_attempts())
print(user_1.increment_login_attempts())
print(user_1.increment_login_attempts())















