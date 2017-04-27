#start with the previous list, and print a message to each of them.  The text
#of each messsage should be the same but each message should be personalized
#with their name
x = 0
ActualFriends = ['Blake', 'Adam', 'Ders']
for i in range(0,3):
    message = 'Hey ' + ActualFriends[x] + ', you are friggin hilarious!'
    print(message)
    x += 1

#for loops sure make this easy
