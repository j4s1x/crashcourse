#GuestList
Guests = ['Nick Offerman', 'Rob Lowe', 'Chevy Chase', 'Wil Wheaton']
def GuestList(a,b): #changing the range as people are added and removed.
    GuestIndex = 0 #Wouldn't let me call this outside the function for some reason.
    #Maybe because I was using a function this time it needed to be in the same scope.
    for i in range(a,b):
        print (Guests[GuestIndex] + ' is invited to my party')
        GuestIndex += 1
#ChangingGuessList:
#One of the guests can't make it.  Need someone else to invite.
#Replace the name of the guest who can't make it with one who can.
#Print a second set of invitations for the ones who can make it
def ChangeList():
    print (Guests[2] + " can't make it to the party!")
    del Guests[2]
    Guests.insert(1,'Sir Patrick Stewart')
    GuestList(0,4)
#More Guests.  Just found a bigger dinner table.  Think of 3 more Guests
#to invite.  Inform all guests you have a bigger table.  Use insert() to add
#one new guest to the beginning, one to the middle, and use append()
#to add one.  Print a new set of invitations
def MoreGuests(): #maybe a way to do this in a loop
    seperator=', '
    Guests.insert(0,'Pumpkin')
    Guests.insert(2,'Willow')
    Guests.insert(-1, 'Moxie')
    print(seperator.join(Guests) + ' are all now invited to the party.')
#Shrinking guest list
#This one is a doozy.  Now only 2 people can come. Use pop() to remove guests, and each pop,
#says their name and not invited.  Then tell the last 2 people they can come.
#Then delete them and print the empty list

def Shrinking():
    count = 0
    for i in range(0,5):
        print(Guests.pop(), end='')
        print(' is unable to make it to the party')
    print (Guests)
    Guests.clear()
    print (Guests)
#Runs the functions
GuestList(0,4)
ChangeList()
MoreGuests()
Shrinking()
