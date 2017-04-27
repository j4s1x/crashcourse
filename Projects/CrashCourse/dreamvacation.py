#make empty dictionary
#poll users asking for name and where they want to visit, store in dictionary
#print nicely

responses = {}
polling_active = True

while polling_active:
    name = input('Please type your name:\n')
    response = input('Where would you like to vacation:\n')

    responses[name] = response #simple way to make this work
    repeat = input('Would you like to make another entry? (yes/no)\n')
    if repeat == 'no':
        polling_active == False
        print('Thank you.')
        break

for name, response in responses.items():
    print(name.title() + ' wants to go to ' + response.title())
#this one below is just simplified to help me visualize how it works adding to dictionaries from input.  The above
#code works great and neat
newdic={}
num_entries = 0
while num_entries <3:
    the_key = input('enter a key')
    the_value = input('enter a value')
    newdic[the_key] = the_value
    num_entries += 1

for the_key, the_value in newdic.items():
    print(the_key + ' is in ' + the_value)
