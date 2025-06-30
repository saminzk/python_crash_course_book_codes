users = {
    'aeinstein':{
        'first_name': "Albert",
        'last_name': "Einstein",
        'location': 'princeton'
    },
    'mcurie':{
        'first_name': 'Marie',
        'last_name': "Curie",
        'location': 'paris'
    }
}


for username, user_info in users.items():
    print("\t username: "+ username)
    full_name = user_info['first_name'] +" "+ user_info['last_name']
    location = user_info['location']

    print("\t Full Name: "+full_name)
    print("\t Location: "+location)