cities = {
    'tokyo':{
        'country': 'Japan',
        'population':'37 million',
        'fact': 'Tokyo is the world’s most populous metropolitan area and has more Michelin-starred restaurants than any other city in the world.'
    },
    'new york':{
        'country': 'United States',
        'population':'8.5 million',
        'fact': 'The iconic Times Square is named after The New York Times newspaper, which moved its headquarters there in 1904.'
    },
    'Paris':{
        'country': 'France',
        'population': '2.1 million',
        'fact': 'There are over 30 replicas of the Eiffel Tower around the world, including ones in Tokyo, Las Vegas, and Shenzhen.'
    }
}


for city,details in cities.items():
    print("city: "+city)
    print("\tCountry: "+details['country'])
    print("\tPopulation: "+details['population'])
    print("\tfact: "+details['fact'])
    print('\n')