# /Users/mcdickenson/github/PS398/HW3/
import unittest
import sorter

class TestListCode(unittest.TestCase):

    def setUp(self):
        self.practiceList = sll.LinkedList(5)
        self.practiceList.addNode(12)
        self.practiceList.addNodeAfter(9,12)
        self.practiceList.addNodeAfter(2, 9)
        self.expectedOutput1 = "practiceList: 5 -> 12 -> 9 -> 2 -> END"


    # correctness tests:


    def test_display_list(self):
        self.assertEqual(print(self.practiceList), self.expectedOutput1)

    
    # robustness tests: 

    def test_bad_start_value(self):
        self.assertEqual(self.badList = sll.LinkedList("five"), "Bad start value. Please enter a start value of type int().")


if __name__ == '__main__':
    unittest.main()
