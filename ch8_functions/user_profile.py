def build_profile(first,middle, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['middle'] = middle
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] =  value
    return profile




user_profile = build_profile('albert','magnitus','einstein',location = 'princeton', field='physics')
print(user_profile)