### IN style_example.py FILE###

#what would you say if you were working with someone and this is the code they gave you?

import math
import sys

def example1():
  #This is a long comment. This should be wrapped to fit within 72 characters
  some_tuple = (1,2,3,'a')
  some_variable={
      "long":"Long code lines should be wrapped within 79 character to prevent page cutoff stuff",
      'other':[
          math.pi, 
          100,
          200, 
          300, 
          9999292929292, 
          "This is a long string that looks gross and goes beyond what it should"],
          "more": {"inner": "This whole logical line should be wrapped"},
          "data": [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5]}
  
  return (some_tuple, some_variable)

def example2(): 
    return {"has_key() is deprecated": True}

class Example3(object):
  def __init__(self, bar):
      if bar:
          bar+= 1 
          bar = bar * bar
          return bar
          
      else:
          some_string = """ Indentation in multiple strings should 
                        not be touched. Only actual code should be 
                        reindented. This is more code. """
                
          return (sys.path, some_string)