#Print the first three, the middle 3, and the last three of a list using slices.

animals = ['cat', 'dog', 'cow', 'horse', 'sheep', 'chicken', 'goat', 'pig', 'alpaca']

print(animals[:3])
print(animals[3:6])
print(animals[-3:])

#Let's make a copy of that list.  One list will be my animals, the other will be a friend's animals
#add a new animal to the friends list but not mine.

buddyAnimals = animals[:]
animals.append('lion')
buddyAnimals.append('Unicorn')
print(animals)
print(buddyAnimals)

#print these lists using a for loop
index = len(animals)-1
print(index)
for i in range(0,index):
    print(animals[i], end='*')
