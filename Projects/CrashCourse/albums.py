#write a function called make_album() that builds a dictionary
#describing a music album.  Should have artist name and album title.  Should
#return a dictionary containing these two pieces of information.  Use function to
#make 3 dictionaries representing different albums.  Print each return value to make sure it works
#Add an optional paramter to make_album that allows you to store the number of tracks on the album.
#if it fits that parameter add it to the dictionary.  Call it at least once.

def make_album(artist_name, artist_title,num_tracks=''):
    #if num_tracks:
    #else:
    #for key, value in album.items():
        #print ('The ' + key.title() +' is ' + value)
    if num_tracks:
        album = {'artist': artist_name, 'title': artist_title, 'tracks': num_tracks}
        print('The album has ' + album['tracks'] + ' tracks on it')
        print('The artist is ' +album['artist'])
        print('Their album is ' + album['title'])
    else:
        album = {'artist': artist_name, 'title': artist_title}
        print('The artist is ' +album['artist'])
        print('Their album is ' + album['title'])
#make_album('Jimi Hendrix', 'Are You Experienced?')
#make_album('Black Sabbath', 'Sabbath Bloody Sabbath')
#make_album('Led Zeppelin', 'Led Zeppelin', '12')
#music = make_album('Jimi Hendrix', 'Are You Experienced?')
#print(music)
#music = make_album('Black Sabbath','Black Sabbath', '6')
#print(music)

def crash_project(artist_name, artist_title, num_tracks=''):
    album ={'artist': artist_name, 'title': artist_title}
    if num_tracks:
        album['tracks'] = num_tracks
    return album
music = crash_project('Jimi Hendrix', 'Are you experienced?', '10')
print(music)
