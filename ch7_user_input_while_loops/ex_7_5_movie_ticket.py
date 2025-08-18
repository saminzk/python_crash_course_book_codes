prompt = "Enter your age: "

while True:
    age = int(input(prompt))
    if age < 3:
        print("Ticket is free.")
    elif age >= 3 and age <12:
        print("Ticket $10.")
    elif age > 12:
        print("Ticket is $15")