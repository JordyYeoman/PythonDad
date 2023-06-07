import utils

# This program prints Hello, world!
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


# Note: The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.
class BigDog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("'Woof' - " + self.name)
    
    def getBreed(self):
        print("Dog breed is: " + self.breed)

doggo = BigDog("Layla", "Maremma")
doggo.bark()
doggo.getBreed()

# Utilising seperate files functions
utils.getSome()
utils.loopOverStuff()

# simple for loop examples
utils.printAllTheThings()

def feedPlz():
  print("BORK, feed me sir.")

feedPlz()