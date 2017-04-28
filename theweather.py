#! python3
#Scrape and print the weather from environment canada

import requests, sys, bs4, os
def current_date():
    res = requests.get('https://weather.gc.ca/city/pages/sk-40_metric_e.html')
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('div dl dd')
    statement = str(elems[1].getText())
    print(str(statement)+ '\n')
res = requests.get('https://weather.gc.ca/city/pages/sk-40_metric_e.html')
res.raise_for_status
soup = bs4.BeautifulSoup(res.text)
elems = soup.select('div dl dd')
statement = str(elems[1].getText()+'.txt')
create_text = open('/home/jason/Projects/weatherlogs/' + str(statement), 'w') #global variable to write and be referenced
#by other functions
create_text.write(str(elems[1].getText()) + '\n')



def current_temp():
    res = requests.get('https://weather.gc.ca/city/pages/sk-40_metric_e.html')
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('div p span')
    print("The current temperature is:")
    print(elems[0].getText())
    create_text.write(str(elems[0].getText())) #TODO this for the rest of the functions

def current_condition():
    res = requests.get('https://weather.gc.ca/city/pages/sk-40_metric_e.html')
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('div dl dd')
    print('The current conditions:')
    print(elems[2].getText() + '\n')
    create_text.write(str(elems[2].getText())) #TODO this for the rest of the functions


def pressure():
    res = requests.get('https://weather.gc.ca/city/pages/sk-40_metric_e.html')
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('div dl dd')
    print('The pressure is:')
    print(elems[3].getText() + 'and ' + elems[5].getText().lower()+ '\n')
    #for i in range(1,159):
        #print(elems[i].getText())

def humidity():
    res = requests.get('https://weather.gc.ca/city/pages/sk-40_metric_e.html')
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('div dl dd')
    print('The humidity is:')
    print(elems[10].getText() + '\n')
    #for i in range(1,159):
        #print(elems[i].getText())

def wind():
    res = requests.get('https://weather.gc.ca/city/pages/sk-40_metric_e.html')
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('div dl dd')
    print('Winds:' + elems[11].getText())
#Main code
print("Weather report as of:")
current_date()
current_temp()
current_condition()
pressure()
humidity()
wind()
#TODO Visibility--don't really care though
#TODO store on a text file
#res = requests.get('https://weather.gc.ca/city/pages/sk-40_metric_e.html')
#res.raise_for_status
#soup = bs4.BeautifulSoup(res.text)
#elems = soup.select('div dl dd')
#statement = str(elems[1].getText()+'.txt')


#write_temp = str(current_temp())
#filename=statement
#create_text = open('/home/jason/Projects/weatherlogs/' + str(filename), 'w')
#create_text.write(write_temp)
