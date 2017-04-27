#five names and fav numbers for each.  print  out the names and the favorite numbers.
#Now each person has more than one favorite number.  Print that out
friends = {
'John Cleese': [1,2,3],
'Terry Gilliam': [42,2,75],
'Michael Palin': [3,234,141],
'Eric Idle': [4,2],
'Terry Jones': [5,13,7]
}
for key, value in friends.items():
    print(key + "'s favorite numbers are:")
    for values in value:
        print ('\t' + str(values))
