#Write a function called city_country that takes in the name of a city and a city_country
#it should return like, 'Santiago, Chile'
#Call function with three city pairs and print

def city_country(city,country):
    formatted_text =(city + ', ' + country)
    return formatted_text.title()
city = city_country('saskatoon','canada')
print(city)
city = city_country('houston','america')
print(city)
city = city_country('edmonton','canada')
print(city)
