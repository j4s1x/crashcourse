class Dog(): #capitalized letters commonly refer to classes in python
    """A simple attempt to model a dog."""  # no arguments the class is created from scratch

    def __init__(self, name, age):
        """Initiate name and attributes."""

        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting!")
    def roll_over(self):
        """Simulate rolling over as a response to a command."""
        print(self.name.title() +  " rolled over!")

my_dog = Dog('Willie',6)
parents_dog = Dog('Moxie', 12)
print('My parents have a dog named ' + parents_dog.name.title())
print('She is ' + str(parents_dog.age) + ' years old.')
parents_dog.sit()
parents_dog.roll_over()
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
