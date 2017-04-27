#make several dictionaries, where the name of each dictionary is the name of a pet
#in each dictionary, include the kind of animal and owner's name.
#store these dictionaries in a list called pets.  Loop through
#the list and print everything about each pet.
pets = []
pet = {'name': 'Pumpkin','type': 'cat', 'owner': 'Chanda'}
pets.append(pet)
pet = {'name': 'Willow', 'type': 'cat', 'owner': 'Jason'}
pets.append(pet)
pet = {'name': 'Moxie', 'type': 'dog', 'owner': 'Jordan'}
pets.append(pet)

for pet in pets:
    print('Here is some info on ' + pet['name']+ ':')
    for key, value in pet.items():
        print (key.upper()+ ': ',value.upper())
#so make an empty master list, then add values to it.  Dont try and make a dictionary
#inside of a list like you did before.
