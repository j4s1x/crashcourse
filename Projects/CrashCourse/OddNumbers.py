#use range() to make a list of the odd numbers from 1 to 20

#numbers=list(range(1,20,2))
#print (numbers)
#Threes
#Make a list of the multiples of 3 from 3 to 30.  Using for loop:

blank=[]
for num in range(3,30,3):
    blank.append(num)
print(blank)

#Cubes.  Make a list of the first 10 cubes.  The integers 1 through 10
#2**3 = the cube of 2

cubes = []
for value in range(1,11):
    cubes.append(value**3)
print (cubes)

#or

squares=[value **2 for value in range(1,11)] #probably the best way to do this.
print (squares)

myNumbers =[num * 4 for num in range(1,30)]
print (myNumbers)
