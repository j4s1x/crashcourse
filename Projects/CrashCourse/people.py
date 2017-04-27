#make 3 dictionaries for 3 different people.  Store these in a list called
#people.  Loop through the list of people.  As it loops print out everything you know about them.

people = []
info = {'name': 'Jason', 'age': '28', 'favorite boardgame': 'chess'}
people.append(info)
info = {'name': 'Chanda', 'age': '27', 'favorite boardgame': 'catan'}
people.append(info)
info = {'name': 'Jordan', 'age': '22', 'favorite boardgame': 'axis and allies'}
people.append(info)
print('Here is some info about 3 people:')
for info in people:
    for key, value, in info.items():
        print(key.upper() + ': ' + value.title())

#for i in people:
#    x = (i['name'] + ' is ' + i['age'] + ' years old and likes ' + i['favorite boardgame'])
#    print(x)

#TODO wish I could sort this.
