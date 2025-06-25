users = ['van','eric','john admin','emily']


for user in users: 
    if 'admin' in user:
        print('Hello admin would you like to see a status report?.')
    else:
        print("Hello "+user+", thank you for logging in again.")

