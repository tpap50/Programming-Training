
import unittest
from unittest.mock import patch 
#import mock
import sys
sys.path.append("/Users/tompapas/Documents/Programming/Programming-Training/MIT6_0001F16/Assignments/Problem Set 2")
import functions
class test_update(unittest.TestCase):
  def test_update(self):
      self.assertEqual(functions.updates(2, "a", ['n'], "marina"), (2,["n","a"],'_ a_ _ na'))
      self.assertEqual(functions.updates(2, "c", ['b'], "marina"), (1,["b","c"], '_ _ _ _ _ _ '))
      self.assertEqual(functions.updates(2, "q", ['b','f'], "marina"), (1,["b","f","q"], '_ _ _ _ _ _ '))
    #def test_validguess(self):
      #valid guess - user enters "f"
    #self.assertEqual(valid_guess.valid_guess('abc', '_ _ _ _ ',3,2), (3, "f", 2)) 
  def test_validguess(self):
      with patch('builtins.input', return_value="f"):
        self.assertEqual(functions.valid_guess('abc', '_ _ _ _ ',3,2), (3, "f", 2))  
      with patch('builtins.input', side_effects=("a","f")):
        self.assertEqual(functions.valid_guess('abc','_ _ _ _',3,2), (3,"f",1))
    #self.assertEqual(valid_guess.valid_guess('abc', '_ _ _ _ ',3,2), (3, "f", 1))
    #letter already guess and there are no warnings, user enters "a", followed by "f", lose a guess.
if __name__ == '__main__':
  unittest.main()
