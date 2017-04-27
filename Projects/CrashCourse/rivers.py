#list rivers and the provinces they run through.  Use a loop to print this out.
#Also print the river and provinces individually
rivers = {
'MacKenzie River': 'Northwest Territories',
'Yukon River': 'British Columbia',
'Saint Lawrence River': 'Ontario',
'Nelson River': 'Manitoba',
'Saskatchewan River': 'Saskatchewan',
}
for river, province in rivers.items():
    print('The ' + river + ' flows through ' + province)
print('The following is the list of rivers from the dictionary:')
for river in rivers:
    print(river)
print('The following is the list of provinces from the dictionary')
for province in rivers.values():
    print(province)
