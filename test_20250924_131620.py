import unittest

class TestCalculateCircleArea(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_valid_input(self):
        self.assertEqual(calculate_circle_area(3.0), 28.2645)
        self.assertAlmostEqual(calculate_circle_area(1.5), 7.0685)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_circle_area(0)
        with self.assertRaises(ValueError):
            calculate_circle_area(-1.5)
        with self.assertRaises(TypeError):
            calculate_circle_area("not a number")

    def test_edge_cases(self):
        self.assertEqual(calculate_circle_area(0), 0)
        self.assertAlmostEqual(calculate_circle_area(1e-6), 5.7758e-12)
        with self.assertRaises(ValueError):
            calculate_circle_area(float('inf'))
        with self.assertRaises(TypeError):
            calculate_circle_area(complex(0, 0))