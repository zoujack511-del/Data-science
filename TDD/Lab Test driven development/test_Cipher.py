import unittest
from Cipher import pattern_cipher # Cipher Rules

class TestPatternCipher(unittest.TestCase): # inherit unittest, a built-in Python framework used 
                                            # to write and run automated tests for code.

# 1.-----If the input is empty ("") or None, it is returned unchanged ------
    def test_none_input(self):
        self.assertIsNone(pattern_cipher(None))
    def test_empty_string(self):
        self.assertEqual(pattern_cipher(""), "")

# 2.-----Only alphabetic words are transformed. ------
    def test_numbers_unchanged(self):
        self.assertEqual(pattern_cipher("123"), "123")
        self.assertEqual(pattern_cipher("#$3"), "#$3")

#3.-----If a word is a palindrome (reads the same forward and backward, case-insensitive), leave it unchanged.---------
    def test_palindrome_lowercase(self):
        self.assertEqual(pattern_cipher("level"), "level")
        self.assertEqual(pattern_cipher("civic"), "civic")

#4.-------- If the word contains any repeated letters and is not a palindrome, reverse the word. --------
    def test_repeated_letters_reverse(self):
        self.assertEqual(pattern_cipher("hello"), "olleh")
        self.assertEqual(pattern_cipher("letter"), "rettel")

#5.-------- If all letters are unique, rotate the word left by one character. --------
    def test_unique_letters_rotate(self):
        self.assertEqual(pattern_cipher("cat"), "atc")
        self.assertEqual(pattern_cipher("Python"), "ythonP")

#6.-------------------------- Rule Priority Example ----------------------------
    def test_palindrome_priority_over_repeated(self):
        self.assertEqual(pattern_cipher("noon"), "noon")

#7.-------------------------- Single-Letter Words ----------------------------
    def test_single_letter(self):
        self.assertEqual(pattern_cipher("a"), "a")

#8.-------------------------- Two-Letter Words ----------------------------
    def test_two_letter(self):
        self.assertEqual(pattern_cipher("ab"), "ba")
        self.assertEqual(pattern_cipher("bb"), "bb")


if __name__ == '__main__':
    print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity = 2) # Verbosity shows detailed test information.

