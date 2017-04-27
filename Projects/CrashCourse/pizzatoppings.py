#Write a loop that asks for pizza toppings until the user types 'quit'
#After each topping, print out the topping saying you are adding to pizza
#Bonus points I'll just make a list and print the list after the user quits :)

all_toppings = []
print ('Please tell me what you would like on your pizza.  You may add no more than 3 toppings:\n')
print ('Exit the program and eat pizza by typing <quit>')
topping_count = 0
done ='Here are all your toppings:\n'
while topping_count <3:
    ask_topping = input('Please tell me what you would like on your pizza:\n')
    if ask_topping == 'quit':
        break
    else:
        print(ask_topping + '!  adding to topping list')
        all_toppings.append(ask_topping)
        topping_count += 1
print(done + ', '.join(all_toppings))
