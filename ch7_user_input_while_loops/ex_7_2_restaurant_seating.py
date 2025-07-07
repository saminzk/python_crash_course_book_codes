prompt = "For how many people do you need table for"

number_of_people = int(input(prompt))

if(number_of_people >= 8):
    print("You will have to wait for the table: ")
else:
    print("Your table is ready.")