import unittest
from src.main.fibonacci_rabbits import fibonacci_rabbits

class FibonacciRabbitsTestCase(unittest.TestCase):
    def test_fibonacci_rabbits_after_one_month_should_be_1(self):
        self.assertEqual(1, fibonacci_rabbits(1))

    def test_fibonacci_rabbits_after_five_months_should_be_8(self):
        self.assertEqual(8, fibonacci_rabbits(5))

    def test_fibonacci_rabbits_after_twenty_month_should_be_10946(self):
        self.assertEqual(10946, fibonacci_rabbits(20))

    def test_fibonacci_rabbits_should_raise_exception_if_months_are_negative(self):
        with self.assertRaises(ValueError):
            fibonacci_rabbits(-2)

if __name__ == '__main__':
    unittest.main()
