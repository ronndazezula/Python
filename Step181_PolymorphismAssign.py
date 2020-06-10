import re
import webbrowser
import time

#parent class
class Animal:
    commonName = None
    family = None
    species = None
    order = None
    organism = 'heterotroph'
    cells = 'without walls'
    state1 = 'alive'
    state2 = 'dead'
    
    def getInfo(self): #method inside parent class with key 'self' to represent the instance of the class and access its attributes and methods
        entry_commonName = input("What animal are you interested in?\n(type your answer in lowercase): >>> ")
        if not re.match("^[a-z]*$", entry_commonName):
            print("Only lowercase letters a-z allowed!")
        else:
            print("\nThe {} is an interesting animal!".format(entry_commonName))
            time.sleep(3) #pause for 3 seconds
            print("\nDid you know this animal is a {}?\n".format(self.organism))
            time.sleep(3)
            print("\nA couple interesting facts about the animal 'cat':")
            time.sleep(2)

#first child class instance
class Cat(Animal):
    commonName = 'domestic cat' #overrides value from parent, if do not remains the same as parent
    family = 'Felidae'
    species = 'Felis catus'
    order = 'Carnivora'
    lifespan = '13-18 years'
    fur = True

#second child class instance
class WildCat(Animal):
    commonName = 'wild cat'
    species = 'Felis sylvestris'
    lifespan = '2-16 years'
    lives = 'outdoors'
    food = 'prey'
    voice = 'roar'
    
    def facts(self):
        msg = "\nA {} is likely to {} and live {} {}.".format(self.commonName,self.voice,self.lifespan,self.lives)
        return msg

#third child class instance
class HouseCat(Animal):
    commonName = 'house cat'
    lifespan = '13-18 years'
    owner = 'varies'
    lives = 'indoors'
    food = 'kibble'
    voice = 'meow'

    def details(self):
        msg = "\nA {} is likely to {} and live {} {}.".format(self.commonName,self.voice,self.lifespan,self.lives)
        return msg
        time.sleep(3)

#fourth child class instance
class SchCat(Animal):
    commonName = 'Schrödinger\'s Cat'
    lifespan = 'Unknown'
    owner = 'Erwin Rudolf Josef Alexander Schrödinger'
    lives = 'in a box'
    food = 'none'
    voice = 'muffled'

    def faq(self):
        msg = "\n\n{}, however, is said to be {} and {} at the same time.\n".format(self.commonName,self.state1,self.state2)
        time.sleep(2)
        webbrowser.open("https://en.wikipedia.org/wiki/Schr%C3%B6dinger%27s_cat") #open info in browser
        return msg

    def paradox(self):
        entry_state = input("Please read the Wikipedia that popped up in your browser.\nWhich do you think, is {} alive or dead?: \n>>> ".format(self.commonName))
        if (entry_state == 'alive'):
            print("\nYou are an optimist!")
        else:
            print("\nHow do you know FOR SURE until you open the box?")

#controls code
if __name__ == "__main__":
    #instantiate each class object, gains access to attributes/values
    ask = Animal()
    ask.getInfo()
    
    wild = WildCat()
    print(wild.facts())

    house = HouseCat()
    print(house.details())

    wave1 = SchCat()
    print(wave1.faq())

    wave2 = SchCat()
    wave2.paradox()
