my_foods = ['pizza','falafel','carrot cake']
friends_foods = my_foods[:]


#this doesn't work
friends_foods = my_foods # both lists get updated

my_foods.append('cannoli')
friends_foods.append('ice cream')

print('My favourite foods are:')
print(my_foods)

print('My frineds favourite foods are:')
print(friends_foods)

