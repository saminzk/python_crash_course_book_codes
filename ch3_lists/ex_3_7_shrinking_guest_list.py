guest_list = ['John','Arya','Sansa','Catherine']


print(f"{guest_list.pop()}, sorry can't invite you to dinner.")
print(f"{guest_list.pop()}, sorry can't invite you to dinner.")

for guest in guest_list: 
    print(f"{guest} is invited to dinner.")


del guest_list[1]
del guest_list[0]

print(f"{guest_list} is invited to dinner now.")