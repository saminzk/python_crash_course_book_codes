guest_list = ['John','Lopez','Sansa']

print(f"{guest_list[0]} is invited to dinner.")
print(f"{guest_list[1]} is invited to dinner.")
print(f"{guest_list[2]} is invited to dinner.")

absent_guest = 'Lopez'
guest_list.remove(absent_guest)

print(f"{absent_guest} will not attend the dinner")

guest_list.append('Arya')

print("New Invitation list")
print(f"{guest_list[0]} is invited to dinner.")
print(f"{guest_list[1]} is invited to dinner.")
print(f"{guest_list[2]} is invited to dinner.")
