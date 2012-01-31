import unittest
import HW1

class TestHW1Code(unittest.TestCase):

    def setUp(self):
        return

    # correctness tests:

    def test_shout_question(self):
        self.assertEqual(HW1.shout("Hello world?"), "HELLO WORLD!")

    def test_reverse_string(self):
        self.assertEqual(HW1.reverse("Bom bard a drab mob."), ".bom bard a drab moB")
        # ("Sore was I ere I saw Eros."), ".sorE was I ere I saw eroS")

    def test_reversewords_string(self):
        self.assertEqual(HW1.reversewords("Hello world."), "world Hello.")

    def test_reversewords_2sentence(self):
        self.assertEqual(HW1.reversewords("Hello world. What's your name?"), "world Hello. name your What's.")   

    def test_reversewordletters_string(self):
        self.assertEqual(HW1.reversewordletters("A civic testset is nice."), "A civic testset si ecin.")

    def test_piglatin_sentence(self): # preserving old test case
        self.assertEqual(HW1.piglatin("pig latin"), "igpe atinle")

    def test_piglatin_sentence(self):
        self.assertEqual(HW1.piglatin("Romans like bacon."), "omansre ikele aconbe")
        
    def test_palindrome_sentence(self):
        self.assertEqual(HW1.reverse("Bom bard a drab mob."), ".bom bard a drab moB")

        ### other tests that would fail:
        ### Dr.
        ### Some ellipses...
        
    # TODO: test some composite functions


    # robustness tests: (I think)

    def test_shout_with_nums(self):
        self.assertEqual(HW1.shout("I like the number 7."), "I LIKE THE NUMBER 7!")

    def test_no_punctuation_rwl(self): 
        self.assertEqual(HW1.reversewordletters("A long string without punctuation"), "A gnol gnirts tuohtiw noitautcnup")


# TODO: some way to preserve punctuation in sentence-level functions
if __name__ == '__main__':
    unittest.main()
