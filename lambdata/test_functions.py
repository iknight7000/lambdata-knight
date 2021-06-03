import pandas as pd
from faker import Faker

fake = Faker()

df = pd.read_csv("https://raw.githubusercontent.com/iknight7000/lambdata-knight/main/Hospitals.csv")

new_addresses = []
for _ in range(10):
    new_addresses.append(fake.address())

class Null_Count:
    """A Null Count class with methods and attributes"""
    # Constructors are used to instantiate an object of the class.
    # The __init__ *keyword* is a method that defines the objects.
    # self arguments reference the instance of the class to interact with itself
    # df is the argument that has to be passed in to the object
    def __init__(self,df):
        """This is a constructor method"""
        self.df = df
        # attributes
        #This is the creation of the attribute
        #We are defining the attribute here
        

    def clean_data(df):
        return df.isnull().sum().sum()



class Add_Series:
    def __init__(self,df):
        self.df = df 

    def list_to_series(list,df):
        df[""] = pd.Series(list)

