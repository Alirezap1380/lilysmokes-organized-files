import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_valid_operations(self):
        self.assertEqual(calculator('+', 3, 2), 5)
        self.assertEqual(calculator('-', 7, 4), 3)
        self.assertEqual(calculator('*', 2, 3), 6)
        self.assertAlmostEqual(calculator('/', 8, 2), 4)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculator('%', 5, 2)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            calculator('+', 'a', 2)
        with self.assertRaises(TypeError):
            calculator('+', 3, 'b')

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calculator('/', 0, 2)

if __name__ == '__main__':
    unittest.main()