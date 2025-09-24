import unittest

class TestDivide(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_division(self):
        self.assertAlmostEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(10, -2), -5.0)
        self.assertAlmostEqual(divide(-10, 2), -5.0)
        self.assertAlmostEqual(divide(-10, -2), 5.0)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            divide(1, 0)
        with self.assertRaises(ValueError):
            divide(-1, 0)
        with self.assertRaises(ValueError):
            divide(0, 1)
        with self.assertRaises(ValueError):
            divide(0, -1)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            divide('a', 'b')
        with self.assertRaises(TypeError):
            divide('a', 1)
        with self.assertRaises(TypeError):
            divide(1, 'b')

if __name__ == '__main__':
    unittest.main()