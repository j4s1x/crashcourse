alien_0 = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
print ('Original x-position: ' + str(alien_0['x-position']))
#move alien to the right
#determine how far to move alien based on current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien.
    x_increment = 3

#new position plus old
alien_0['x-position'] = alien_0['x-position'] + x_increment
print('New x-position: ' + str(alien_0['x-position']))

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
