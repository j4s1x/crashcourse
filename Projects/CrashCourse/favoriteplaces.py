#make a dictionary called favorite places.  Think of 3 names to use as keys
#store one to three favorite places for each person.  Ask some friends to
#name a few of their favorite places Loop through and print.
favorite_places = {
'Jason': ['Scotland', 'Norway', 'Canada'],
'Chanda':['BC', 'Ecuador', 'Egypt'],
'Jordan':['Phillipines'],
'Pumpkin':['My lap'],
'Willow':['The counter', 'The tree']
}

for name, place in favorite_places.items():
    print(name + "'s " + 'favorite places are...')
    for places in place:
        print ('\t' + places.title())
