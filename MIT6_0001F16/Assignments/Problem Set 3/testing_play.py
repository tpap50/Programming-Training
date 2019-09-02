
import unittest
import sys
sys.path.append("/Users/tompapas/Documents/Programming/Programming-Training/MIT6_0001F16/Assignments/Problem Set 3")
import functions_play
class test_update(unittest.TestCase):
  def testget_word_score(self):
    self.assertEqual(functions_play.get_word_score("it",7), 2)
 
if __name__ == '__main__':
  unittest.main()
