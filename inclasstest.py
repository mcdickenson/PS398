import unittest
import inclass

class TestInClassCode(unittest.TestCase):

    def setUp(self):
        return

    def test_one(self): # a correctness test
        self.assertEqual(inclass.ordinalnum(1), "1st")

    def test_eleven(self):
        self.assertEqual(inclass.ordinalnum(11), "11th")

    #def test_string(self): # a robustness test
        #self.assertRaises(inclass.ordinalnum("one"), TypeError)

    def test_negative(self):
        self.assertEqual(inclass.ordinalnum(-3), "-3rd")

if __name__ == '__main__':
    unittest.main()
