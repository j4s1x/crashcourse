#store the names of your friends in a list called names.
#print each person's name in the list
#by accessing each element in the list, one at a time

friends = ["you", "don't", "have", "any", "friends"]
print (friends[0])
print (friends[1])
print (friends[2])
print (friends[3])
print (friends[4])

#So that was one long complicated annoying way to type a lot of code
#let's try this way instead it was easier
def FriendList(x):
    for i in range(0,5):
        print (friends[x])
        x += 1
FriendList(0)

#way less complicated.  And in a cute little function too :)
