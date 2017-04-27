#A theater charges different prices depending on a person's age
#if they are under 3, its free
#if they are between 3 and 12, its 10 dollars
#if they are over 12 it's 15 dollars
#write loop asking their age and telling them the cost
#Feel like a loop isn't necessary here...but w/e
while True:
    age = input('Please enter your age to determine ticket price\n')
    age = int(age)
    if age < 3:
        print ('You are a small, small child.  You get in for free.  Next!')
    elif age >3 and age <12:
        print('You are a regular child.  10 dollars please.  Next!')
    else:
        print('You are a full grown adult.  15 dollars please.  Next!')
