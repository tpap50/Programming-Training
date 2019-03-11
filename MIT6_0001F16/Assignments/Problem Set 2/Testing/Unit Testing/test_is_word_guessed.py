import unittest
import sys
sys.path.append("/Users/tompapas/Documents/Programming/Programming-Training/MIT6_0001F16/Assignments/Problem Set 2")
import solution

class test_solution(unittest.TestCase):
  """docstring for ClassName"""
  def test_iswordguessed(self):
    self.assertEqual(solution.is_word_guessed("marina",[]), False)
    self.assertEqual(solution.is_word_guessed("marina",["a","b","c"]), False)
    self.assertEqual(solution.is_word_guessed("marina",["a","r","i","m", "n"]), True)
    self.assertEqual(solution.is_word_guessed("marina",["a","r","i","m", "N"]), False)
  def test_getguessword(self):
    self.assertEqual(solution.get_guessed_word("marina",[]), "_ _ _ _ _ _ ")
    self.assertEqual(solution.get_guessed_word("marina",["m","a"]), "ma_ _ _ a")
    self.assertEqual(solution.get_guessed_word("marina",["m","a","a"]), "ma_ _ _ a")
    self.assertEqual(solution.get_guessed_word("marina",["m","a","a","r","n","i"]), "marina")
  def test_getavailableletters(self):
    self.assertEqual(solution.get_available_letters(['m','a','r','i','n','a']), 'bcdefghjklopqstuvwxyz')
    self.assertEqual(solution.get_available_letters(['m','a','r','i','2','1']), 'bcdefghjklnopqstuvwxyz')
    self.assertEqual(solution.get_available_letters([]), 'abcdefghijklmnopqrstuvwxyz')
  #def test_validinput(self):
  # self.assertEqual(solution.valid_input('m', "m_ _ _ _ _ ", "5", 3, 3 ),(3, 'g', 2))
  # self.assertEqual(solution.valid_input('m', "m_ _ _ _ _ ", "m", 3, 3 ),(3, 'g', 2))
  # self.assertEqual(solution.valid_input('m', "m_ _ _ _ _ ", "#", 3, 0 ),(2, 'g', -1))
  # self.assertEqual(solution.valid_input('m', "m_ _ _ _ _ ", "m", 3, 0 ),(2, 'g', -1))

  


if __name__ == '__main__':
  unittest.main()
    