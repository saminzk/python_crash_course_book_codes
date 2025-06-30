persons = [{
    'first_name': 'John',
    'last_name': 'Volkin',
    'age':'33',
    'city': 'Sydney'
},{
    'first_name': 'Jen',
    'last_name': 'Willis',
    'age':'27',
    'city': 'Boston'
},{
    'first_name': 'Kent',
    'last_name': 'Clarke',
    'age':'31',
    'city': 'London'
},{
    'first_name': 'Abigail',
    'last_name': 'Martin',
    'age':'27',
    'city': 'Los Angeles'
}]


for person in persons:
        full_name = person['first_name'] +" "+ person['last_name']+"."
        age = person['age']
        location = person['city']

        print("Name: "+full_name)
        print("Age: "+age)
        print("Location: "+location)
        print("\n")