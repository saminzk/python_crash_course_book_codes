pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra Cheese','peperoni']
}



print("You have ordered a "+pizza['crust']+" crust pizza.")

for topping in pizza['toppings']:
    print('\t '+topping)