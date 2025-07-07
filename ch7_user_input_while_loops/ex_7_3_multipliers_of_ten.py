prompt = "Enter a number: "

number = int(input(prompt))


if number % 10 == 0:
    print(str(number)+" is a multiplier of 10")
else:
    print(str(number)+"is not a multiplier of 10")