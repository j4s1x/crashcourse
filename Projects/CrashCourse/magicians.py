#make a list of magicians names.  Pass the list to a function called show_magicians()
#which prints the name of each magician in the list 8-9
def show_magicians(magician):
    for magicians in magician:
        print (magicians)
#modify the list by adding 'the Great' to each magician, made a new list just like the book did
#this was the next part of the excercise 8-11
def make_great(magician):
    while magician:
        new_list = magician.pop()
        new_magician.append(new_list + ' the Great')
    for magi in new_magician:
        print (magi)
def mod_current_list(magician):
    for magicians in magician:
        magician = magicians + ' the great'
        print(magician)  #There we go, so this is 8-10
magician = ['Harry Houdini', 'David Copperfield', 'David Blaine', 'Teller', 'Pen Jillette']
new_magician=[]
show_magicians(magician)
make_great(magician)
mod_current_list(magician)
