import unittest

class TestSubtract(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_subtract_integers(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-3, 4), -7)
        self.assertEqual(subtract(0, 0), 0)

    def test_subtract_non_integers(self):
        with self.assertRaises(ValueError):
            subtract(5, "2")
        with self.assertRaises(ValueError):
            subtract("5", 2)
        with self.assertRaises(ValueError):
            subtract(5.0, 2)
        with self.assertRaises(ValueError):
            subtract(-3.0, "4")
        with self.assertRaises(ValueError):
            subtract("0", 0)
        with self.assertRaises(ValueError):
            subtract(5, complex(0, 0))
        with self.assertRaises(ValueError):
            subtract(complex(0, 0), 5)

    def test_subtract_negative_integer(self):
        self.assertEqual(subtract(-3, -4), 1)
        self.assertEqual(subtract(-3, -3), 0)
        self.assertEqual(subtract(-3, -2), 1)

    def test_subtract_zero(self):
        self.assertEqual(subtract(x, 0) for x in (-5, 0, 5))

if __name__ == "__main__":
    unittest.main()