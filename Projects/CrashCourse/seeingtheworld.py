#Think of five places in the world you would like to visit
#Print the list in its original order
#use sorted() to print in alphabetical
#show it is still in original order by printing it
#use sorted() to print in backwards alphabetical
#show it is still in original order
#use reverse() sort() and sort() changing the order permanently

places =['UK', 'China', 'Scotland', 'Colorado', 'Denmark']
print(places)

def sort_forward():
    print(sorted(places))
    print(places)
def sort_backward():
    print(sorted(places, reverse = True))
    print(places)
sort_forward()
sort_backward()
