# make a list of people who should take the favorite languages poll
#Include some names in the dictionary and some that aren't
#loop through the list of people who should take the poll
#if they have taken it, personally thank them
#elif tell them to take the poll
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['john cleese', 'terry gilliam', 'michael palin', 'jen', 'sarah', 'edward', 'phil']
for name in friends:
    if name in favorite_languages:
        print (name.title() + ' has taken the poll.  Thank you very much')
    elif name not in favorite_languages:
        print(name.title() + ' needs to take the poll!')
        
