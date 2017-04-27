#use a dictionary to store info about someone.  first, last name, age, city.  Print.

person = {'first_name': 'jason', 'last_name': 'williams', 'age': 28, 'city': 'saskatoon'}

print('Your name is ' + person['first_name'].title() + ' ' + person['last_name'].title() + '.')
print('You are ' + str(person['age']) + ' years old.')
print('You live in ' + person['city'].title())

#simple enough
