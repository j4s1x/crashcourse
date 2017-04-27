#make a list of the numbers 1 to 1 million, then use a for loop to print the numbers
#how about just up to 100 so I don't blow up my computer
numbers=[]
add=1
for i in range(0,100):
    numbers.append(add)
    add +=1
print (numbers)
print (sum(numbers))
#or

y=list(range(1,101))
print (y)
print(sum(y))
x = list(range(1,6))
print (x)
