#alien just shot down.  Create variable and assign it a color
#Test whether it is green.  If it is they get five points
#write one version that passes and one that fails

#alien_color = 'red'
#if alien_color == 'green':
#    print('You get 5 points')
#elif alien_color == 'red':
#    print('You get 10 points!')
#    alien_color = 'blue'

#if alien_color=='green':
#    print('five more points')
#else:
#    print('The alien is actually ' + str(alien_color))

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings: #so i am seeing that requested_topping is each item within the list
        print('adding ' + requested_topping + '.')
    print ('Finished making pizza')
else:
    print('\n are you sure you want a plain pizza')
