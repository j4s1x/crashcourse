#Allow user to enter artist and album title to dictionary as in albums.py
album = {} #had a problem when this dictionary was in the function itself.  Should be global.
def make_album():
    print ("type 'q' to quit at any time")
    while True:
        the_artist = input('Please enter an artist name:\n')
        if the_artist == 'q':
            break
        the_title = input('Please enter an album they have\n')
        if the_title == 'q':
            break
        album[the_artist] = the_title
    return album
info = make_album()

for key, value in album.items():
    print('the artist is ' + key.title() + ' and the album is ' + value.title())
