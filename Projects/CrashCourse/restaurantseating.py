#ask how many people are in the dinner group
#if more than 8, say they have to wait for a table.
guests = input('Welcome to Shitty Wok.  Table for how many?\n')
guests = int(guests)
if guests > 8:
    print(str(guests) + '!?  No room for you right now.  You wait!')
else:
    print ('Prease prease you sit now!')
