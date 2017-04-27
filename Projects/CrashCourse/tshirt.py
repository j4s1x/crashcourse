#write a func make_shirt() that accepts the size and text of a message that should be
#printed on a shirt.  Print a message sumarizing the size and text on shirt
#call once using positional arguments, then using keyword arguments
#large_shirts using default arguments
def make_shirt(size='large', text='I Love Monty Python'):
    print('The size of the shirt is ' + size)
    print('The text on the shirt reads ' + text)
make_shirt(size ='medium', text= 'eyes up here')
make_shirt(text = 'turn around',  size = 'small')
make_shirt()
