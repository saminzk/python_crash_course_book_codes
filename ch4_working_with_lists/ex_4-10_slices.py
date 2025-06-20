foods = ['pizza','falafel','carrot cake','ice cream','canoli','burger','cheese cake','sphagetti','salami']

print("The first three items in list are: ")
for food in foods[:3]:
    print(food)

print("\nThe middle three items in list are:")
for food in foods[3:6]:
    print(food)

print("\nThe last three items are:")
for food in foods[6:9]:
    print(food)