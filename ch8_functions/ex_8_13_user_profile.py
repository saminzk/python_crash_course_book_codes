def build_profile(fname, lname, **infos):
    profile = {}
    profile['fname'] = fname
    profile['lname'] = lname
    for key,value in infos.items():
        profile[key] = value
    return profile


user_profile = build_profile('Samin','Khan',profession='Software Engineer', location='Dhaka',favourite_language='python')

print(user_profile)