# message = input("Tell me something and I will repeat it back to you: ")

# print(message)


prompt = "Tell me something and will repeat it back to you.:"
prompt = "\nEnter 'quit' to end the program. "

active = True
message = ""

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
