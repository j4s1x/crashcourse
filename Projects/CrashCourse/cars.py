#write a function that stores information about a car in a dictionary.
#should be manufacturer, model name, and arbitrary amount of arguments
#call function with two other name-value pairs such as color or chrome rims or whatever

def cars(model, name, **features):
    the_cars = {}
    the_cars['model'] = model
    the_cars['name'] = name
    for key, value in features.items():
        the_cars[key] = value
    return the_cars
first_car = cars('ford','focus', chrome_rims = 'no')
second_car = cars('chevy', 'impala', chrome_rims = 'yes', fake = 'no', color = 'red')

print(first_car)
print(second_car)
