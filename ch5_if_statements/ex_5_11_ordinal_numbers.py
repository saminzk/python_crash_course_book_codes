numbers = []

for val in range(1,10):
    numbers.append(val)

for num in numbers:
    if(num == 1):
        print("1st")
    elif (num == 2):
        print("2nd")
    elif (num == 3):
        print('3rd')
    else:
        print(f"{num}th")