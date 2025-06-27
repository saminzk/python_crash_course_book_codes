favorite_languages = {
    'jen': 'Java',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}

friends=['phil','sarah']

# for name, language in favorite_languages.items():
#     print(name.title()+"'s favorite language is "+language+".")

# for name in favorite_languages.keys():
#     print(name.title())

# for langs in favorite_languages.values():
#     print(langs.title())

# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         print("Hi "+name.title()+", I see your favorite language is "+favorite_languages[name].title()+"!")

# if "erin" not in favorite_languages.keys():
#     print("Erin please take our poll.")

# for name in sorted(favorite_languages.keys()):
#     print(name.title()+", thank you for taking the poll.")

for language in favorite_languages.values():
    print(language)