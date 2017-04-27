#make a dictionary called cities.  Use the names of three cities as keys in your dictionary.
#Create a dictionary about each city and include the country it is in, its
#approximate population, and one fact about that city.  The key's for each city's
#dictionary should be something like country, population, and fact.
#Print the name of each city and all it's information stored about it.
cities = {
'saskatoon':{'country': 'canada', 'population': 222190,'fact':'everyone is a bunch of hicks.'},
'london':{'country': 'uk', 'population':8674000,'fact': 'rooty tooty point n shooty.'},
'stockholm':{'country': 'sweden', 'population':940000,'fact': 'I want to live there.'}
}
for city, city_info in cities.items():
    country = city_info['country'] #helps to assign variables to different dictionary calls
    pop = city_info['population']
    a_fact = city_info['fact']
    print ('Here is some info about ' + city.title() + ':')
    print('it is located in ' + country.title())
    print('It has a population of ' + str(pop))
    print('A random fact about ' + city.title() +' is:\n' + a_fact.title())
