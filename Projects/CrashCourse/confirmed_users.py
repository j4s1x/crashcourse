#Start with users that need to be verified
#and an empty list to hold the confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#verify each user until there are no more unconfirmed_users
#move each verified user into the confirmed users list

while unconfirmed_users: #this is running as long as unconfirmed_users is not empty
    current_user = unconfirmed_users.pop() #.pop() removes and returns the user so it still exists
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

#display all confirmed users

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print (confirmed_user.title())
