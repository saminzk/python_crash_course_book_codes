favorite_number = {
    'John': ['1','40','2'],
    'Jason': ['13','20'],
    'Clara': ['7','69']
}



for name, number in favorite_number.items():
    print("Participant name: "+name)
    print("favorite numbers:")
    for num in number:
        print(num)