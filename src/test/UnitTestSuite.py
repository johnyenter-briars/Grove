import unittest 
import sys
import os
from ..services.DatabaseService import DatabaseService

class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):   
        d = DatabaseService()

if __name__ == '__main__': 
    unittest.main() 
