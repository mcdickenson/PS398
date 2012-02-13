# /Users/mcdickenson/github/PS398/HW3/
import unittest
import sll

class TestListCode(unittest.TestCase):

    def setUp(self):
        self.practiceList = sll.LinkedList(5)
        self.practiceList.addNode(12)
        self.practiceList.addNode(9)
        self.practiceList.addNode(2)
        self.expectedOutput1 = "5 -> 12 -> 9 -> 2 -> END"


    # correctness tests:


    def test_display_list(self):
        self.assertEqual(str(self.practiceList), self.expectedOutput1)

    
    # robustness tests: 

    # def test_bad_start_value(self):
        # self.assertEqual(sll.LinkedList("five"), "Bad start value. Please enter a start value of type int().")


if __name__ == '__main__':
    unittest.main()
