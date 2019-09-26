
import unittest
import sys
sys.path.append("/Users/tompapas/Documents/Programming/Programming-Training/MIT6_0001F16/Assignments/Problem Set 3")
import functions_play

words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
             ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
             ("fork", 7):209, ("FORK", 4):308}
 


class test_update(unittest.TestCase):
  def testget_word_score(self):
    for (word, n) in words.keys():
    	score=words[(word,n)]
        print((word,n))
        print(score)
        self.assertEqual(functions_play.get_word_score(word,n), score)

if __name__ == '__main__':
  unittest.main()
