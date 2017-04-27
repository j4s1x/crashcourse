#ask the user for a number and say if it is a multiple of ten
number = input('Type a number and I will say if it is a multiple of ten:\n')
number=int(number)
if number % 10 == 0:
    print(str(number) + ' is a multiple of 10!')
else:
    print(str(number) + ' is not a multiple of 10')
