"""OOP example for Sprint 1 Module 2"""
import pandas
import numpy
class BareMinimumClass:
    pass



class Car:
    """A car class with methods and attributes"""
    # Constructors are used to instantiate an object of the class.
    # The __init__ *keyword* is a method that defines the objects.
    # self arguments reference the instance of the class to interact with itself
    # self, max_speed, color are arguments that have to be passed in to the object
    def __init__(self, max_speed, color):
        """This is a constructor method"""
        # attributes
        #This is the creation of the attribute
        #We are defining the attribute here
        self.max_speed = max_speed
        self.color = color
    
    # A function inside a class is a method
    def changeColor(self, new_color):
        """This is a method"""
        #Methods perform actions on attributes
        #Here we are changing the color 
        self.color = new_color
    
    
    def changesColorToGreen(self):
        """Calling methods using self keyword"""
        self.changeColor(new_color="Green")



class SocialMediaUser:
    """This is a social media user class"""
    #Since upvotes has a defined value, it can be skipped
    def __init__(self, name, location, upvotes=0):
        """
        Constructor will have a default upvotes value of 0
        Unless specficied otherwise in instantiation.
        """
        # reference attributes through <object>.<attribute>
        self.name = str(name)  # <object>.name
        self.location = str(location)  # <object>.location
        self.upvotes = int(upvotes)  # <object>.upvotes
    
    #This function lets the user receive a number of upvotes
    def receive_upvotes(self, num_upvotes=1):
        """Method that changes upvotes attribute"""
        self.upvotes += num_upvotes
    
    #is should return a boolean/binary value
    def is_popular(self):
        """Method that returns True or False depending on upvotes condition"""
        return self.upvotes > 100
    
    # __repr__ changes what's printed when just object is running
    def __repr__(self):
        """Changes what is printed out when running just the object"""
        return f"<name: {self.name}, upvotes: {self.upvotes}>"



# Example of Inheritance
class Animal:
    """Parent Class"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = str(diet_type)
        # Adjusted Attribute
        self.adjusted_weight = float(weight + 100)
    def run(self):
        return "Vroom, Vroom, me quick!"
    def eat(self, food):
        return f"Huge fan of that {food}"



class Sloth(Animal):
    """Child class of Animal class"""
    def __init__(self, name, weight, diet_type, num_naps=10038):
        super().__init__(name, weight, diet_type)
        self.num_naps = num_naps
    def say_something(self):
        """Says a witty pun"""
        return "This is a sloth of typing"
    def run(self):
        return "I am a slow guy - I don't run!"
# print("I get printed no matter what")

# A python internal, reserved name that is executed only if name is main
if __name__ == "__main__":
    # print("I have been executed via python cli")
    # print("This is not printed upon import")
    # SocialMediaObject:
    user1 = SocialMediaUser(name="Carl", location="The Congo")
    user2 = SocialMediaUser(name="Carlitta", location="Djibouti", upvotes=200)
    user3 = SocialMediaUser(name="George Washington",
                            location="Russia", upvotes=10)
    print("{} has {}".format(user1.name, user1.upvotes))
    print("{} has {}".format(user2.name, user2.upvotes))
    print("{} has {}".format(user3.name, user3.upvotes))
    print(f"is User3 popular? ANS: {user3.is_popular()}")
    user3.receive_upvotes(100)  # Geroge Washington should now have 110 upvotes
    print(f"is User3 popular? ANS: {user3.is_popular()}")