responses = {}


#set flag to indicate that polling is active
polling_active =  True


while polling_active:
    #Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("which mountain would  you like to climb someday?")

    #store the data from input the the responses dictionary
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        polling_active = False


#show results
print("\n<--------Poll Results------->")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
