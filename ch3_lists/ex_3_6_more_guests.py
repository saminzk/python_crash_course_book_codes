guest_list = ['John','Arya','Sansa']


guest_list.insert(0,'Sam')

guest_list.insert(2,'Jane')

guest_list.append('Catherine')


for guest in guest_list: 
    print(f"{guest} is invited to dinner.")