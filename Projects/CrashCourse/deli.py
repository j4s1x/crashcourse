#make list called sandwich_orders fill with various sanswiches
#make list called finished_sandwiches
#loop through each sandwich in orders and say you are making it
#add it to finished sandwiches and print result
sandwich_orders = ['grilled cheese', 'monte cristo', 'reuben', 'club', 'panini', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []
print ('sorry we are out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    the_sandwich = sandwich_orders.pop()
    print('Making sandwich: ' + the_sandwich)
    finished_sandwiches.append(the_sandwich)
for sandwich in finished_sandwiches:
    print('Here is your ' + sandwich)
