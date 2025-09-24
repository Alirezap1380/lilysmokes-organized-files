import unittest

class TestMultiply(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_multiply_int_int(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-3, -4), 12)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_int_float(self):
        self.assertEqual(multiply(3, 4.5), 13.5)
        self.assertEqual(multiply(-3, -2.5), 7.5)
        self.assertEqual(multiply(0, 2.5), 0)

    def test_multiply_float_int(self):
        self.assertEqual(multiply(4.5, 3), 13.5)
        self.assertEqual(multiply(-2.5, -3), 7.5)
        self.assertEqual(multiply(2.5, 0), 0)

    def test_multiply_float_float(self):
        self.assertEqual(multiply(4.5, 3.5), 15.75)
        self.assertEqual(multiply(-2.5, -3.5), 8.75)
        self.assertAlmostEqual(multiply(1.00001, 2), 2.00002, delta=0.00001)

    def test_type_error(self):
        self.assertRaises(TypeError, multiply, 3, 'non-numeric')
        self.assertRaises(TypeError, multiply, 'non-numeric', 4)