#Make a class called restaurant.  The init method should store the name and cuisine type
#Make an instance called restaurant from your class, print the 2 attributes individually
#and then call both methods

class Restaurant():

    def __init__ (self, name, cuisine):

        self.name = name
        self.cuisine = cuisine
    def describe_restaurant(self):
        print("The restaurant is called " + self.name.title())
        print("They serve " + self.cuisine.title() + " cuisine.")
    def open(self):
        print(self.name.title() + ' is open for business!')

willows = Restaurant('the willows', 'italian')
willows.open()
willows.describe_restaurant()
