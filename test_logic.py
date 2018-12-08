import unittest
from calc import add, subtract, multiply, divide, square

class TestCalc(unittest.TestCase):
    """
    Test class for calc.py module
    """

    def test_add(self):
        """
        Test add() fonction.
        
        """
        res = add(3,2)
        self.assertEqual(res, 5)


    def test_subtract(self):
        """
        Test subtract() function.
        """
        res = subtract(3,2)
        self.assertEqual(res, 1)

    def test_subtract_negatives(self):
        """
        Test subtract() function with negative numbers as inputs.
        """
        res = subtract(-1, -2)
        self.assertEqual(res, 1)

    def test_subtract_positive_and_negative(self):
        """
        Test subtract() function with a positive and a negative input.
        """
        res = subtract(2,-1)
        self.assertEqual(res, 3)

    def test_subtract_positive_and_negative(self):
        """
        Test subtract() function with a negative and a positive input.
        """
        res = subtract(-2, 1)
        self.assertEqual(res, -3)



if __name__ == '__main__':
    unittest.main()