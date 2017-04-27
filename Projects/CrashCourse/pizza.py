pizza = ['Hawaiian', 'Deluxe', 'Chicken Bacon Ranch']
def favorites():
    for i in range(0,3):
        print('I like ' + pizza[i] + ' pizza!')
    x=","
    print(str(x.join(pizza[0:2])+ ' and ' + pizza[2])+ ' are my absolute favorite!')
favorites()
#Animals...part2
#Think of 3 different animals with common characteristic
#print a statement about each animal using a for loop
#add a line at the end saying what they have in common
animals = ['Housecat', 'Lion', 'Tiger']
def common():
    y=','
    for z in range(0,3):
        print('a ' + animals[z] + ' would make a great house pet!')
    animals.clear()
    animals.extend(['Housecats', 'Lions', 'Tigers'])
    print(str(y.join(animals[0:2]) + ' and ' + animals[2]) + ' like to wreck your house!')
common()
