def make_pizza(size,*toppings):
    print("Making a "+str(size)+" - inch pizza with following toppings:")
    for topping in toppings:
        print("- "+topping)
    # print(type(toppings))


# make_pizza(16,'peperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')