toppings = []
topping = print("Enter a topping to add to the pizza")
while (True):
    topping = input("Enter a topping: ")
    if(topping == 'quit'):
        break
    toppings.append(topping)
    print(f"You added {topping} as topping.")



