import unittest

class TestSquareNumber(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_square_number_valid_float(self):
        self.assertEqual(square_number(3.0), 9.0)

    def test_square_number_valid_integer(self):
        self.assertEqual(square_number(5), 25)

    def test_square_number_negative_float(self):
        self.assertEqual(square_number(-2.5), 6.25)

    def test_square_number_zero(self):
        self.assertEqual(square_number(0), 0)

    def test_square_number_non_numeric_type(self):
        with self.assertRaisesRegex(ValueError, "Input must be a numeric type."):
            square_number("invalid")

if __name__ == '__main__':
    unittest.main()