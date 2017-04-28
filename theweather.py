#! python 3
"""Would like to add the ability to write to text files as a database"""
import requests, sys, bs4, os
res = requests.get('https://weather.gc.ca/city/pages/sk-40_metric_e.html')
res.raise_for_status
soup = bs4.BeautifulSoup(res.text)
class Weather():
    def __init__ (self, data_type, elements, location):
        self.data_type = data_type
        self.elements = elements
        self.location = location
    def data(self):
        print(self.data_type)
        elems = soup.select(self.elements)
        print(elems[self.location].getText().strip())
date = Weather('Current date and time:', 'div dl dd', 1)
temperature = Weather('Temperature:','div p span', 0)
current_condition = Weather('Current Conditions:','div dl dd', 2)
pressure = Weather('Pressure:', 'div dl dd', 3)
humidity = Weather('Humidity:', 'div dl dd', 10)
wind = Weather('Wind speed:', 'div dl dd', 11)
date.data()
temperature.data()
current_condition.data()
pressure.data()
humidity.data()
wind.data()
