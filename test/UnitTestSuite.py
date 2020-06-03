import unittest 
import sys
import os
sys.path.append(".")
from services.DatabaseService import DatabaseService

"""This unit test MUST be run from the src directory using:
    python test/UnitTestSuite.py
"""
class TestDBConnection(unittest.TestCase): 
  
    def test(self):   
        d = DatabaseService()
        assert('Thomas' == d.getStudent(1).getFirstName())

if __name__ == '__main__': 
    unittest.main() 
