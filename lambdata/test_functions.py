import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/iknight7000/lambdata-knight/main/Hospitals.csv")

class Null_Count:
    """A Null Count class with methods and attributes"""
    # Constructors are used to instantiate an object of the class.
    # The __init__ *keyword* is a method that defines the objects.
    # self arguments reference the instance of the class to interact with itself
    # df is the argument that has to be passed in to the object
    def __init__(self,df):
        """This is a constructor method"""
        # attributes
        #This is the creation of the attribute
        #We are defining the attribute here
        

    def clean_data(df):
        return df.isnull().sum().sum()

print(Null_Count.clean_data(df))