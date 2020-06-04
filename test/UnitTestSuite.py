import unittest 
import sys
import os
sys.path.append(".")
from services.DatabaseService import DatabaseService

"""This unit test MUST be run from the src directory using:
    python test/UnitTestSuite.py
"""
class TestDBConnection(unittest.TestCase): 
  
    def test_firststudent_thomas(self):   
        d = DatabaseService()
        self.assertEqual('Thomas', d.getStudent(1).getFirstName())

    def test_numprojects_three(self):
        d = DatabaseService()
        self.assertEqual(3, len(d.getProjects()))

if __name__ == '__main__': 
    unittest.main() 
