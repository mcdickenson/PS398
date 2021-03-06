# /Users/mcdickenson/github/PS398/HW4/
import unittest
import sll

class TestListCode(unittest.TestCase):

    def setUp(self):
        self.practiceList = sll.LinkedList(5)
        self.practiceList.addNode(12)
        self.practiceList.addNode(9)
        self.practiceList.addNode(2)
        self.expectedOutput1 = "5 -> 12 -> 9 -> 2 -> END"
        self.nonUniqueList = sll.LinkedList(1)
        self.nonUniqueList.addNode(2)
        self.nonUniqueList.addNode(1)
        self.lotsOfTwos = sll.LinkedList(1)
        self.lotsOfTwos.addNode(2)
        self.lotsOfTwos.addNode(3)
        self.lotsOfTwos.addNode(2)
        self.lotsOfTwos.addNode(4)
        self.lotsOfTwos.addNode(2)
        self.lotsOfTwos.addNode(5)
        self.lotsOfTwos.addNode(2)
        self.lotsOfTwos.addNode(6)

    # correctness tests:

    def test_display_list(self):
        self.assertEqual(str(self.practiceList), self.expectedOutput1)

    def test_unique_list_false(self):
        x = self.nonUniqueList.checkUniqueValue(1)
        self.assertEqual(x, False)

    def test_unique_list_true(self):
        x = self.nonUniqueList.checkUniqueValue(2)
        self.assertEqual(x, True)

    def test_add_node_after(self):
        self.practiceList.addNodeAfter(13,12)
        self.expectedOutput2 =  "5 -> 12 -> 13 -> 9 -> 2 -> END"
        self.assertEqual(str(self.practiceList), self.expectedOutput2)

    def test_add_node_before(self):
        self.practiceList.addNodeBefore(7,12)
        self.expectedOutput3 =  "5 -> 7 -> 12 -> 9 -> 2 -> END"
        self.assertEqual(str(self.practiceList), self.expectedOutput3)

    def test_remove_node(self):
        self.practiceList.removeNode(12)
        self.expectedOutput4 = "5 -> 9 -> 2 -> END"
        self.assertEqual(str(self.practiceList), self.expectedOutput4)

    def test_remove_by_value(self):
        self.lotsOfTwos.removeNodesByValue(2)
        self.expectedOutput5 = "1 -> 3 -> 4 -> 5 -> 6 -> END"
        self.assertEqual(str(self.lotsOfTwos), self.expectedOutput5)

    def test_remove_node_value_at_list_head(self):
        self.lotsOfTwos.head.value = 2
        self.lotsOfTwos.removeNodesByValue(2)
        self.expectedOutput7 = "3 -> 4 -> 5 -> 6 -> END"
        self.lotsOfTwos.length +=1
        self.assertEqual(str(self.lotsOfTwos), self.expectedOutput7)

    def test_reverse_list(self):
        self.practiceList = self.practiceList.reverse()
        self.expectedOutput6 = "2 -> 9 -> 12 -> 5 -> END" 
        self.assertEqual(str(self.practiceList), self.expectedOutput6)

    def test_non_cyclical_list(self):
        self.assertEqual(self.practiceList.hasCycle(), False)

    def test_cyclical_list(self):
        self.practiceList.tail.next = self.practiceList.head
        self.assertEqual(self.practiceList.hasCycle(), True)
    
    # robustness tests: 

    #def test_bad_start_value(self):
        #self.assertEqual(str(sll.LinkedList("five")), "Bad start value. Please enter a start value of type int().")


if __name__ == '__main__':
    unittest.main()
