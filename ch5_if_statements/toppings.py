# requested_toppings = 'mushrooms'

# if requested_toppings != 'anchovies':
#     print("Hold the anchovies!")

# requested_toppings = ['mushrooms','green pepper','extra cheese']


# requested_toppings=[]

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         if(requested_topping == 'green pepper'):
#             print('Sorry, we are out of green peppers.')
#         else:
#             print(f"Adding {requested_topping} to your pizza.")
# else:
#     print('Are you sure you want a plain pizza.')

available_toppings = ['mushrooms','olives','green peppers','peperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry, we don't have "+requested_topping+".")

print("\nFinished making your pizza.")