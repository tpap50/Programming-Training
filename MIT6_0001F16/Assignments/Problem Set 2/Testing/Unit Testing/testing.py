import unittest
import sys
sys.path.append("/Users/tompapas/Documents/Programming/Programming-Training/MIT6_0001F16/Assignments/Problem Set 2")
import print_messages

class test_print_messages(unittest.TestCase):
  """docstring for ClassName"""
  def test_print_messages(self):
    self.assertEqual(print_messages.print_messages(2,2,"a"), None)
    self.assertEqual(print_messages.print_messages(2,2,""), None)
  


if __name__ == '__main__':
  unittest.main()
    
