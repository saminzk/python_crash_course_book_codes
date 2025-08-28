def get_formatted_name(first_name,last_name, middle_name = ''):
    """"return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name
    else:
        full_name = f"{first_name} {last_name}"
        return full_name



musician = get_formatted_name('John','Hooker', 'Lee')
print(musician)

print(get_formatted_name("Jimi","Hendrix"))