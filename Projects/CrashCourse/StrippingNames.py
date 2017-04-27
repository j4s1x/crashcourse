#Store a person's name, include some whitespace characters at the beginning and end
#of their name.  Use \t and \n at least once.
#print the name once so the whitespace is around them, then print the name using
#lstrip(), rstrip(), and strip()
name = "      Jas\ton W\nilliams   "
def whitespace():
    print (name)
    print (name.lstrip())
    print (name.rstrip())
    print (name.strip())


whitespace()

#It's weird, but I tested it and it works.  
