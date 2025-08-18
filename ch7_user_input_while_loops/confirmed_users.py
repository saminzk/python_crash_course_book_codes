unconfirmed_users = ['alice','brian','candace']

confirmed_users = []


#Verify each users until there are no more unconfirmed users.
#Move each verified user into list of confirmed

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying users: {current_user.title()}")
    confirmed_users.append(current_user)


#Display all confirmed users
print("\nThe following users have been confirmed.")
for confirmed in confirmed_users:
    print(confirmed)
