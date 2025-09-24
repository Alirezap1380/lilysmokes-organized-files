import unittest

class TestAddNumbers(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_numbers_with_integers(self):
        self.assertEqual(add_numbers(5, 3), 8)

    def test_add_numbers_with_different_types(self):
        self.assertIsNone(add_numbers(5, "3"))
        self.assertIsNone(add_numbers("5", 3))

    def test_add_numbers_with_none(self):
        self.assertIsNone(add_numbers(None, 3))
        self.assertIsNone(add_numbers(5, None))

    def test_add_numbers_with_floats(self):
        self.assertAlmostEqual(add_numbers(5.0, 3.0), 8.0)
        self.assertIsNone(add_numbers("5.0", 3))
        self.assertIsNone(add_numbers(5, "3.0"))

    def test_add_numbers_with_lists(self):
        self.assertIsNone(add_numbers([1, 2, 3], [4]))
        self.assertIsNone(add_numbers([5], [4, 3]))

if __name__ == "__main__":
    unittest.main()