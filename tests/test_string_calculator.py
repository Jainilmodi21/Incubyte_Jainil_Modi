import unittest
from src.string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_string_calculator(self):
        #test for empty string
        self.assertEqual(add(""), 0)

        #test for 1 and 2 numbers
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("1,2"), 3)

        #test for \n delimeter
        self.assertEqual(add("1\n2,3"), 6)

        #for invalid input
        with self.assertRaises(ValueError) as ctx:
            add("1,\n")
            self.assertEqual(str(ctx.exception), "invalid input")

        self.assertEqual(add("//|\n4|5|6"), 15)

       

if __name__ == '__main__':
    unittest.main()
