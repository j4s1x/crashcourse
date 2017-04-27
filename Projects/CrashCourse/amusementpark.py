#admission for anyone under 4 is free
#admission for anyone between 4 and 18 is $5
#admission for anyone 18 and older is 10$

age = int(input('What is your age\n'))
if age <=4:
    price = 'free'
elif age >=4 and age <18:
    price = 'five dollars'
elif age >= 65:
    price = 5
else:
    price  = 'ten dollars'

print('you are ' + str(price))

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('adding mushrooms')
if 'pepperoni' in requested_toppings:
    print ('adding pepperoni')
if 'extra cheese' in requested_toppings:
    print ('adding extra cheese')
print('\n finished making your pizza')
