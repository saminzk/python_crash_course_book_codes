age = 32
price = 0
if age  < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
# else: 
#     price = 5

print(f"Your admission fee is {price}$.")