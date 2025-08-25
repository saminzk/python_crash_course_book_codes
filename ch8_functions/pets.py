def describe_pet(pet_name,animal_type="dog"):
        print("I have a "+animal_type+".")
        print("My "+animal_type+"'s name is "+pet_name+".")
        print("\n")



# describe_pet('hamster','harry')
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry',animal_type='hamster')
# describe_pet('willie','cat')

# equivalent function calls

#A dog named willie
describe_pet('willie')
describe_pet(pet_name='willie')


#A hamster named harry

describe_pet('harry','hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


describe_pet() #will throw error