def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        msg = 'hello ' + name.title() + '!'
        print (msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
