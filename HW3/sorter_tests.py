# /Users/mcdickenson/github/PS398/HW3/
import unittest
import sorter

class TestSorderCode(unittest.TestCase):

    def setUp(self):
        self.nearly_sorted = [1,3,2,4,5,7,8,6,10,9]
        self.correct_nearly_sorted = [1,2,3,4,5,6,7,8,9,10]
        self.few_unique = [1,2,3,4,1,2,3,4,1,2,3,4]
        self.correct_few_unique = [1,1,1,2,2,2,3,3,3,4,4,4]
        self.reversed = [10,9,8,7,6,5,4,3,2,1]
        self.correct_reversed = self.correct_nearly_sorted
        self.random = [] # TODO: add this, with a set.seed()

    # correctness tests:

    def test_selection_nearly_sorted(self):
        x = sorter.selection(self.nearly_sorted)
        self.assertEqual(x, self.correct_nearly_sorted)

    def test_selection_few_unique(self):
        x = sorter.selection(self.few_unique)
        self.assertEqual(x, self.correct_few_unique)

    def test_selection_reversed(self):
        x = sorter.selection(self.reversed)
        self.assertEqual(x, self.correct_reversed)

    def test_quick3_nearly_sorted(self):
        x = sorter.quick3(self.nearly_sorted)
        self.assertEqual(x, self.correct_nearly_sorted)

    def test_quick3_few_unique(self):
        self.assertEqual(sorter.quick3(self.few_unique), self.correct_few_unique)

    def test_quick3_reversed(self):
        self.assertEqual(sorter.quick3(self.reversed), self.correct_reversed)

        # TODO: add tests for self.random

    
    # robustness tests: 

        # TODO: give it input that isn't a list (say, tuple) and check


if __name__ == '__main__':
    unittest.main()
