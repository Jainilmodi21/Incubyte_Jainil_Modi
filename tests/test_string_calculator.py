import unittest
from src.string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_string_calculator(self):
        #test for empty string
        self.assertEqual(add(""), 0)

        #test for 1 and 2 numbers
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("1,2"), 3)

if __name__ == '__main__':
    unittest.main()
