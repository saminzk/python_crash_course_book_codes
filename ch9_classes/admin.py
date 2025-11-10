from user import User

class Admin(User):
    def __init__(self, first_name,last_name, date_of_birth,city, state, country, privileges = None):
        super().__init__(first_name, last_name, date_of_birth, city, state, country)
        self.privileges = Privileges(privileges)
    
    


class Privileges:
    def __init__(self, privileges = None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_1 = Admin('Samin','Khan','21-NOV-1998', 'Adelaide','South Australia','Australia',['can add post','can delete post','can ban user'])


admin_1.greet_user()
admin_1.describe_user()
admin_1.privileges.show_privileges()