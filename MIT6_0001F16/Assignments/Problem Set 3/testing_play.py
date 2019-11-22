
import unittest
import sys
sys.path.append("/Users/tompapas/Documents/Programming/Programming-Training/MIT6_0001F16/Assignments/Problem Set 3")
import ps3test

words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
             ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
             ("fork", 7):209, ("FORK", 4):308}
 
hand={'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
new_hand={'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}


class test_update(unittest.TestCase):
  def testget_word_score(self):
    for (word, n) in words.keys():
      score=words[(word,n)]
     #   print((word,n))
     #   print(score)
      self.assertEqual(ps3test.get_word_score(word,n), score)
  def testupdate_hand(self):
    self.assertEqual(ps3test.update_hand(hand,'quail'),new_hand)

if __name__ == '__main__':
  unittest.main()
