# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'C',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# print("Sarah's favorite language is "+
#       favorite_languages['sarah'].title()+
#       ".")

favorite_language = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell']
}


for name,languages in favorite_language.items():
    print(f"\n"+name.title()+"'s favorite languages are:")

    for language in languages:
        print('\t'+ language.title())