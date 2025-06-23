banned_users = ['andrew','carolina','david']

user = 'david'

if user not in banned_users:
    print(f"{user.title()} , you can post a response as your wish.")
else:
    print("Sorry, You cant publish any response.")