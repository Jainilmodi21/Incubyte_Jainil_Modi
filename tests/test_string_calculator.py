import unittest
from src.string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_string_calculator(self):

        calc = StringCalculator()
        #test for empty string
        self.assertEqual(calc.add(""), 0)

        #test for 1 and 2 numbers
        self.assertEqual(calc.add("1"), 1)
        self.assertEqual(calc.add("1,2"), 3)

        #test for \n delimeter
        self.assertEqual(calc.add("1\n2,3"), 6)

        #for invalid input
        with self.assertRaises(ValueError) as ctx:
            calc.add("1,\n")
            self.assertEqual(str(ctx.exception), "invalid input")

        #for custom delimeter
        self.assertEqual(calc.add("//|\n4|5|6"), 15)

        #for negative numbers
        with self.assertRaises(ValueError) as ctx:
            calc.add("1,-2,3")
        self.assertEqual(str(ctx.exception), "negatives not allowed: -2")


        #count the number of add calls
        self.assertEqual(calc.get_called_count(), 7)


       

if __name__ == '__main__':
    unittest.main()
