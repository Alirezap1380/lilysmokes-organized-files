import unittest

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fibonacci_with_valid_positive_integer(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        # Add more positive integer test cases as needed

    def test_fibonacci_with_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_with_negative_integer(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-2)
        # Add more negative integer test cases as needed

    def test_fibonacci_with_non_integer(self):
        with self.assertRaises(TypeError):
            fibonacci("invalid")
        with self.assertRaises(TypeError):
            fibonacci(1.5)
        # Add more non-integer test cases as needed

if __name__ == "__main__":
    unittest.main()