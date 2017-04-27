def factors(num):
    factor=1
    for factor_return in range(0,num):
        if num % factor ==0:
            print (factor_return+1)
        factor+=1
factors(1201)
