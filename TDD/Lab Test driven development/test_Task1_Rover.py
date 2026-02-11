'''
    Student shall write their names here
        1. Student 1: Mingjia Zou
        2. Student 2: Geng Yuan
'''

import unittest
from Task1_Rover import rovar

class test_string(unittest.TestCase):

    def setUp(self):
        '''
            Set up shared resources = Class instance to access rover class methods
        '''
        self.rv = rovar()
#-------------------------------------------------------------------------------------------------------#
        self.lower_consonants = "bcdfghjklmnpqrstvwxz" 
        self.upper_consonants = "BCFDGHJKLMNPQRSTVWXZ" 
        self.lower_vowels = "aeiouyåäö"
        self.upper_vowels = "AEIOUYÅÄÖ"
        self.numbers = "0123456789"
        self.specials = "!\"#€%&/(),."
#--------------------------------------------------------------------------------------------------------#
    # Example test case to check lower case rover
    def test_enrove_small(self):
       # self.assertEqual(self.rv.enrove('b'), 'bob')

    # You can continue writing your test cases here based on the assignment description
#--------------------------------------enrove text-------------------------------------------------------#
       expected = ''.join([c + 'o' + c for c in self.lower_consonants])
       self.assertEqual(self.rv.enrove(self.lower_consonants), expected)

    # Test case to check upper case rover
    def test_enrove_upper(self):
       expected = ''.join([c + 'o' + c for c in self.upper_consonants])
       self.assertEqual(self.rv.enrove(self.upper_consonants), expected)

    # Test case to check lower case vowels,should be unchanged
    def test_enrove_lowercase_vowels(self):
        self.assertEqual(self.rv.enrove(self.lower_vowels), self.lower_vowels)

    # Test case to check upper case vowels,should be unchanged
    def test_enrove_uppercase_vowels(self):
        self.assertEqual(self.rv.enrove(self.upper_vowels), self.upper_vowels)

    # Test numbers,should be unchanged
    def test_enrove_numbers(self):
        self.assertEqual(self.rv.enrove(self.numbers), self.numbers)

    # Test Punctuation and Special Characters
    def test_enrove_special_characters(self):
        self.assertEqual(self.rv.enrove(self.specials), self.specials)

    # Test Null Input
    def test_enrove_null_input(self):
        self.assertIsNone(self.rv.enrove(None)) # should return none
    
    # Test empty string
    def test_enrove_empty_string(self):
        self.assertEqual(self.rv.enrove(""), "")

    def test_enrove_mixed_string_example(self):
        self.assertEqual(self.rv.enrove("ahfjbu#$%^"), "ahohfofjojbobu#$%^") #https://www.xn--rvarsprket-75a1r.se/

#--------------------------------------derove text-------------------------------------------------------#
    def test_derove_null_input(self):
        self.assertIsNone(self.rv.derove(None))

    def test_derove_empty_string(self):
        self.assertEqual(self.rv.derove(""), "")

    def test_derove_lowercase_consonants_all(self):
        encoded = self.rv.enrove(self.lower_consonants)
        self.assertEqual(self.rv.derove(encoded), self.lower_consonants)

    def test_derove_uppercase_consonants_all(self):
        encoded = self.rv.enrove(self.upper_consonants)
        self.assertEqual(self.rv.derove(encoded), self.upper_consonants)

    def test_derove_vowels_numbers_specials(self):
        s = self.lower_vowels + self.upper_vowels + self.numbers + self.specials
        self.assertEqual(self.rv.derove(s), s)

    def test_derove_examples(self):
        self.assertEqual(self.rv.derove("ahohfofjojbobu#$%^"), "ahfjbu#$%^")       
#-----------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity = 2)