#Ordinal numbers indicate their position in a list.  Store the numbers 1 through 9 in a list.  1st 2nd 3rd etc.  Loop through
#the list
#use an if elif else chain to print the proper ordinal for each number.

numbers = [1,2,3,4,5,6,7,8,9]
increment = 0
for num in numbers:
    print(numbers[increment])
    increment += 1
    if 1 in increment:
        print increment






#now print the ordinals
#increment = 1
#for i in numbers:
#    if increment == 1:
#        print('1st')
#        increment += 1
#    elif increment == 2:
#        print('2nd')
#        increment +=1
#    elif increment == 3:
#        print('3rd')
#        increment +=1
#        for i in numbers:
#            print (str(numbers[increment]) + 'th')
#            increment += 1
