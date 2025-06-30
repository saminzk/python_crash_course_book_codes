favorite_places = {
    'john':{
        'place': 'Grand Canyon',
        'country': 'USA'
    },
    'Adam': {
        'place': 'Mount Everest',
        'country': 'Nepal'
    },
   'Sadiq': {
        'place': 'Burj Khalifa',
        'country': 'Dubai, UAE'
    }
}

for friend,site in favorite_places.items():
    print(f"{friend}'s favorite place is the {site['place']}, It is situated in {site['country']}.")
