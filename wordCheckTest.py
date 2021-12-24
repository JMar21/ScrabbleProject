import unittest
from wordCheck import wordCheck


class WordCheckTests(unittest.TestCase):
    def test_WordCheck(self):
        #Test valid word with repeated letters
        hand = {"A":3,"C":1,"N":1,"D":1}
        temp = ["C","A","A","A","N","D"]
        #Test valid word
        self.assertTrue(wordCheck(temp,hand))
        hand = {"A": 3, "C": 1, "N": 1, "D": 1}
        temp = ["C","A","N"]
        #Test empty input
        self.assertTrue(wordCheck(temp,hand))
        hand = {"A": 3, "C": 1, "N": 1, "D": 1}
        temp = []
        self.assertFalse(wordCheck(temp, hand))
        #Test invalid word
        hand = {"A": 3, "C": 1, "N": 1, "D": 1}
        temp = ["D","A","M"]
        self.assertFalse(wordCheck(temp, hand))
        # Test invalid word with repeated letters
        hand = {"A": 3, "C": 1, "N": 1, "D": 1}
        temp = ["C", "A", "N","N","N"]
        self.assertFalse(wordCheck(temp, hand))
        #Test invalid word where len(temp)>count(hand)
        hand = {"W":2,"O":1}
        temp = ["W","W","O","W"]
        self.assertFalse(wordCheck(temp, hand))
if __name__ == '__main__':
    unittest.main()
