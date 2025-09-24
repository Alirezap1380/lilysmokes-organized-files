import unittest

class TestAddFunction(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_int_int(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_int_float(self):
        with self.assertRaises(TypeError):
            add(2, 3.0)

    def test_add_float_int(self):
        with self.assertRaises(TypeError):
            add(2.0, 3)

    def test_add_string_int(self):
        with self.assertRaises(TypeError):
            add("2", 3)

    def test_add_int_string(self):
        with self.assertRaises(TypeError):
            add(2, "3")

    def test_add_list_int(self):
        with self.assertRaises(TypeError):
            add([2], 3)

    def test_add_int_list(self):
        with self.assertRaises(TypeError):
            add(2, [3])

    def test_add_non_integer_raises_valueerror(self):
        with self.assertRaises(ValueError) as context:
            add("a", "b")
        self.assertEqual(str(context.exception), "Both arguments should be integers.")

if __name__ == "__main__":
    unittest.main()