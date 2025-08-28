def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()



while True:
    print("Enter q to quit...")
    first_name = input("Enter first name: ")
    if first_name == 'q':
        break
    last_name = input("Enter last name: ")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name, last_name)
    print(f"Hello, {formatted_name}.")