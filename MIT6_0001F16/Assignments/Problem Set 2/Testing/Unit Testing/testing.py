
import unittest
from unittest.mock import patch 
#import mock
import sys
sys.path.append("/Users/tompapas/Documents/Programming/Programming-Training/MIT6_0001F16/Assignments/Problem Set 2")
import functions
class test_update(unittest.TestCase):
  def test_print_messages(self):
    self.assertEqual(functions.print_messages(2,"a"), None)
    self.assertEqual(functions.print_messages(2,""), None)
    self.assertEqual(functions.print_messages(2,"a"), None)
    self.assertEqual(functions.print_messages(2,""), None)
  def test_iswordguessed(self):
    self.assertEqual(functions.is_word_guessed("marina",[]), False)
    self.assertEqual(functions.is_word_guessed("marina",["a","b","c"]), False)
  def test_getavailableletters(self):
    self.assertEqual(functions.get_available_letters(['m','a','r','i','2','1']), 'bcdefghjklnopqstuvwxyz')
    self.assertEqual(functions.get_available_letters([]), 'abcdefghijklmnopqrstuvwxyz') 
  def test_update(self):
      self.assertEqual(functions.updates(2, "a", ['n'], "marina"), (2,["n","a"],'_ a_ _ na'))
      self.assertEqual(functions.updates(2, "c", ['b'], "marina"), (1,["b","c"], '_ _ _ _ _ _ '))
      self.assertEqual(functions.updates(2, "q", ['b','f'], "marina"), (1,["b","f","q"], '_ _ _ _ _ _ '))
      #guess in secret word 
      self.assertEqual(functions.updates(2, "a", ['n'], "marina"), (2,["n","a"],'_ a_ _ na'))
      #guess is a vowel not in secret word
      self.assertEqual(functions.updates(2, "u", ['b'], "marina"), (0,["b","u"], '_ _ _ _ _ _ '))
      #guess not in secret word and not a vowel
      self.assertEqual(functions.updates(2, "q", ['b','f'], "marina"), (1,["b","f","q"], '_ _ _ _ _ _ '))
    #def test_validguess(self):
      #valid guess - user enters "f"
    #self.assertEqual(valid_guess.valid_guess('abc', '_ _ _ _ ',3,2), (3, "f", 2)) 
  def test_validguess(self):
  #guess a letter not guessed so far  
    with patch('builtins.input', return_value="f"):
        self.assertEqual(functions.valid_guess('abc', '_ _ _ _ ',3,2), (3, "f", 2))  
  #guess a letter already guessed followed by one not guessed so far with number of warnings is greater than zero 
    with patch('builtins.input', side_effect=("a","f")):
        self.assertEqual(functions.valid_guess('abc','_ _ _ _',3,2), (3,"f",1))
   #guess a letter already guessed followed by one not guessed so far - reduce the number of warnings to zero and lose a guess   
    with patch('builtins.input', side_effect=("a","b","c","f")):
        self.assertEqual(functions.valid_guess('abc','_ _ _ _',3,2), (2,"f",0))
    #guess a letter already guessed followed by one not guessed so far - reduce the number of warnings to zero and guesses to one   
    with patch('builtins.input', side_effect=("a","b","c","b","f")):
        self.assertEqual(functions.valid_guess('abc','_ _ _ _',3,2), (1,"f",0))
     #guess a letter already guessed followed by one not guessed so far - reduce the number of warnings to zero and lose all guesss   
    with patch('builtins.input', side_effect=("a","b","c","b","c")):
        self.assertEqual(functions.valid_guess('abc','_ _ _ _',3,2), (0,"",0))
     #guess a letter already guessed followed by two  numbers and finally a valid guessir - reduce the number of warnings to zero   
    with patch('builtins.input', side_effect=("a","b","1","2","f")):
        self.assertEqual(functions.valid_guess('abc','_ _ _ _',3,2), (1,"f",0))
    ##guess a letter already guessed followed by two  numbers and finally a valid guessir - reduce the number of guessess to zero   
    with patch('builtins.input', side_effect=("a","b","1","2","3","4")):
        self.assertEqual(functions.valid_guess('abc','_ _ _ _',3,2), (0,"",0))
    with patch('builtins.input', side_effect=("u","o","m")):
        self.assertEqual(functions.valid_guess("abc",'_ _ _ _',3,2), (3,"u",2))  
#        guess a letter already guessed followed by two  numbers and finally a valid guessir - reduce the number of guess to zero and return null   
#    with patch('builtins.input', side_effect=("a","b","1","2","3","4")):
#        self.assertEqual(functions.valid_guess('abc','_ _ _ _',3,2), (0,"",0))
    #s
    #sself.assertEqual(valid_guess.valid_guess('abc', '_ _ _ _ ',3,2), (3, "f", 1))
    #letter already guess and there are no warnings, user enters "a", followed by "f", lose a guess.
  def test_hangman(self):
  #guess the secred word with all correct guesses  
    with patch('builtins.input', side_effect=("t","o","m")):
        self.assertEqual(functions.hangman("tom"), (["","t","o","m"],6,True))  
   #guess the secred word with an incorrect guess   
    with patch('builtins.input', side_effect=("t","o","u", "m")):
       self.assertEqual(functions.hangman("tom"), (["","t","o","u","m"],3,True))  
   #guess the secred word with an incorrect guess and an invalid guess  
#    with patch('builtins.input', side_effect=("t","u", "o","t","m")):
  #      self.assertEqual(functions.hangman("tom"), (["","t","u","o","m"],0,True))  
 #

if __name__ == '__main__':
  unittest.main()
