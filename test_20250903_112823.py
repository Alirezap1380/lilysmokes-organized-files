import unittest

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fibonacci_default_value(self):
        result = fibonacci()
        expected = [0, 1, 1, 2, 3, 5, 8, 13]
        self.assertListEqual(result, expected)

    def test_fibonacci_specific_value(self):
        result = fibonacci(20)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
        self.assertListEqual(result, expected)

    def test_fibonacci_negative_value(self):
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_fibonacci_zero_value(self):
        with self.assertRaises(ValueError):
            fibonacci(0)

    def test_fibonacci_one_value(self):
        result = fibonacci(1)
        expected = [0, 1]
        self.assertListEqual(result, expected)

if __name__ == '__main__':
    unittest.main()