def build_profile(first, last, **user_info):
    #build a dictionary containing everything we know about the user
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',location = 'princeton', field = 'physics')
print(user_profile)
another_profile = build_profile('test','testing',time='night')
print(another_profile)
