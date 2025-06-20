pizzas = ['margherita','peperoni','bbq chicken']

friend_pizzas = pizzas[:] #[:] created a new copy of the existing list


pizzas.append('Meat lovers')
friend_pizzas.append('Spicy Italian')

# print(pizzas)
# print(friend_pizzas)

print("\nMy favourite ")
for pizza in pizzas:
    print(pizza)

print("\nFriends favourite")
for pizza in friend_pizzas:
    print(pizza)