#Make a list of five or more usernames
#they will be loggin in to a system, print a message depending on who logs in
#if admin logs in, give them a special message

#user = ['John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Graham Chapman']
#   user=[]
#admin=['John Cleese']
#log = str(input('Please enter your username:\n'))
#if admin[0] in log:
#    print ('hello admin')
#elif any(user in log for user in user): #need to look into how this works
#    print('hello user')
#elif not user:
#    print('No users found in list.  We need to find some users!')
#else:
#    print('invalid user')

#now a new excercise.  2 lists.  Make sure there is at least one replica in both.  Check to seeing
#if replicates and if so, must print a new username.  Case insensitive.
current_users = ['John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Graham Chapman']
new_users = ['Your mother', 'Rick Sanchez', 'Morty Smith', 'Scary Terry', 'Birdperson', 'Squanchy']
current_users = [i.lower() for i in ['John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Graham Chapman']]
new_users = [j.lower() for j in ['jOhN CleEse', 'Rick Sanchez', 'Morty Smith', 'Scary Terry', 'Birdperson', 'Squanchy']]
for new_user in new_users:
    if new_user in current_users:
        print('duplicate user please try again.')
    else:
        print('list accepted')
#This one was tricky, and I feel it will come up alot and I know how to do it now.  
