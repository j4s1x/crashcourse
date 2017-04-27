#write a function called describe city() that accepts the name of a city and its country
#the function should print a sentence like 'reykjavik is in iceland'
#give the parameter for the country a default value.  Call your function
#for 3 different cities, at least one of which is not in the default country.

def describe_city(city, country = 'canada'):
    print(city.title() + ' is located in ' + country.title())

describe_city('saskatoon')
describe_city('edmonton')
describe_city('Vancouver')
describe_city('Houston','Texas')
