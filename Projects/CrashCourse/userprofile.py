def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first #argument 'first' is now dictionary first name is whatever the arg is
    profile['last_name'] = last #last is now dictionary last name and the value is whatever the arg is
    for key, value in user_info.items():
        profile[key] = value    #returns key and value as a key and value for **user_info
    return profile      #can use key, value as ** means multiples for dictionary
buildme = build_profile('jason', 'williams',
                        location = 'saskatoon',
                        field = 'cooking',
                        time = '4:31 PM')
print(buildme)
