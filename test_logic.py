import unittest
from calc import add, subtract, multiply, divide, square

class TestCalc(unittest.TestCase):
    """
    Test class for calc.py module
    """

    def test_add(self):
        """
        Test add fonction.
        
        """
        res = add(3,2)
        self.assertEqual(res, 5)


if __name__ == '__main__':
    unittest.main()