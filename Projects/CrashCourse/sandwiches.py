###Using return function###

def make_sandwich(*ingredients):
    print('Making sandwich using the following ingredients:')
    while ingredients:
        return ingredients
prepare = make_sandwich('tomato', 'cheese', 'brocolli','chicken')
print (prepare)

###OR without return###

def make_another(*ingredients):
    print("I am making a sandwich using the following ingredients:")
    for ingredient in ingredients:
        print ('--' + ingredient.title())
make_another('bread','lettuce','tomato')
