import unittest
import sys
sys.path.append("/Users/tompapas/Documents/Programming/Programming-Training/MIT6_0001F16/Assignments/Problem Set 2")
import print_messages
import functions
import valid_guess

class test_print_messages(unittest.TestCase):
  """docstring for ClassName"""
  def test_print_messages(self):
    self.assertEqual(print_messages.print_messages(2,2,"a"), None)
    self.assertEqual(print_messages.print_messages(2,2,""), None)
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
  def test_validguess(self):
    self.assertEqual  
if __name__ == '__main__':
  unittest.main()
    
