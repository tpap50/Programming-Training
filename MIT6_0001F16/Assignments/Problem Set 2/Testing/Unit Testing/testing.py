import unittest
from unittest.mock import patch 
#import mock
import sys
sys.path.append("/Users/tompapas/Documents/Programming/Programming-Training/MIT6_0001F16/Assignments/Problem Set 2")
import functions


class test_print_messages(unittest.TestCase):
  """docstring for ClassName"""
  def test_print_messages(self):
    self.assertEqual(functions.print_messages(2,"a"), None)
    self.assertEqual(functions.print_messages(2,""), None)
  def test_iswordguessed(self):
    self.assertEqual(functions.is_word_guessed("marina",[]), False)
    self.assertEqual(functions.is_word_guessed("marina",["a","b","c"]), False)
    self.assertEqual(functions.is_word_guessed("marina",["a","r","i","m", "n"]), True)
    self.assertEqual(functions.is_word_guessed("marina",["a","r","i","m", "N"]), False)
  def test_getguessword(self):
    self.assertEqual(functions.get_guessed_word("marina",[]), "_ _ _ _ _ _ ")
    self.assertEqual(functions.get_guessed_word("marina",["m","a"]), "ma_ _ _ a")
    self.assertEqual(functions.get_guessed_word("marina",["m","a","a"]), "ma_ _ _ a")
    self.assertEqual(functions.get_guessed_word("marina",["m","a","a","r","n","i"]), "marina")
  def test_getavailableletters(self):
    self.assertEqual(functions.get_available_letters(['m','a','r','i','n','a']), 'bcdefghjklopqstuvwxyz')
    self.assertEqual(functions.get_available_letters(['m','a','r','i','2','1']), 'bcdefghjklnopqstuvwxyz')
    self.assertEqual(functions.get_available_letters([]), 'abcdefghijklmnopqrstuvwxyz')
  def test_update(self): 
    self.assertEqual(functions.updates(2, "a", ['n'], "marina"), (2,["n","a"],'_ a_ _ na'))
    self.assertEqual(functions.updates(2, "c", ['b'], "marina"), (1,["b","c"], '_ _ _ _ _ _ '))
    self.assertEqual(functions.updates(2, "q", ['b','f'], "marina"), (1,["b","f","q"], '_ _ _ _ _ _ '))
  def test_validguess(self):
    with patch('builtins.input', return_value="f"):
      self.assertEqual(functions.valid_guess('abc', '_ _ _ _ ',3,2), (3, "f", 2))  
    #letter already guess - user enters "a" followed by "f" have 2 warnings so lose one 
    #self.assertEqual(valid_guess.valid_guess('abc', '_ _ _ _ ',3,2), (3, "f", 1))
    #letter already guess and there are no warnings, user enters "a", followed by "f", lose a guess.
    #self.assertEqual(valid_guess.valid_guess('abc', '_ _ _ _ ',3,0), (2, "f", 0))
    #enters a number, user enters 5, followed by "f", has a warning remaining and loses it.
    #self.assertEqual(valid_guess.valid_guess('abc', '_ _ _ _ ',3,1), (3, "f", 0))
    #enters a number, user enters 10, followed by "h", didnt have a warning so loses a guess.
    #self.assertEqual(valid_guess.valid_guess('abc', '_ _ _ _ ',3,1), (2, "h", 0))
if __name__ == '__main__':
  unittest.main()
