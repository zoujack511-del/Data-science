# The purpose of this unit test is to automatically verify that the add function 
# in the calc module returns the expected result. 

import unittest
import calc

class TestCalc(unittest.TestCase): # define a test class, named TestCalc, 
                                   # TestCalc is a subclass of unittest.TestCase. (inheritance)
                                   # self.assertEqual(a, b)
                                   # self.assertTrue(x)
                                   # self.assertIn(a, b)
                                   # self.setUp()
                                   # self.tearDown()
    def test_add(self):  # define a test, only start by test can be recogonized by unittest
        self.assertEqual(calc.add(10, 5), 15) # an assert, the result expected to be 15
        self.assertEqual(calc.add(-1, -5), -6)
        self.assertEqual(calc.add(-10, 10), 0)

    def test_substract(self):  
        self.assertEqual(calc.substract(10, 5), 5) 
        self.assertEqual(calc.substract(-1, -5), 4)
        self.assertEqual(calc.substract(-10, 10), -20)


# terminal :  python -m unittest test_calc.py   

if __name__ == '__main__': # checks whether the Python file is being run directly as the main program.
    unittest.main()        # starts the unittest test runner and executes all discovered test cases in the current file.  