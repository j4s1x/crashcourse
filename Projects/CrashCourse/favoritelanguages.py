favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']

for name, value in sorted(favorite_languages.items()):
    print(name.title() + "'s'" + ' favorite language is ' +  value.title()+ '.')
print('\n')
for person in sorted(favorite_languages):
    print(person.title())
    if person in friends:
        print('\tHi ' + person.title() + ', I see your favorite language is ' + favorite_languages[person].title() + ' !')
if 'erin' not in favorite_languages:
    print('Erin!  Please take our poll!')
print('The following languages have been mentioned:')
for language in sorted(set(favorite_languages.values())):
    print (language.title())

favorite_languages = {
'jen': ['python', 'ruby', 'english', 'french'],
'sarah':['c', 'german'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print (name.title() + "'s' favorite languages are:")
    for language in languages:
        print('\t' + language.title())
