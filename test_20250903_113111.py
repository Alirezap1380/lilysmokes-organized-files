import unittest

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_positive_small(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(11), 89)
        self.assertEqual(fibonacci(12), 144)
        self.assertEqual(fibonacci(13), 233)
        self.assertEqual(fibonacci(14), 377)
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(16), 987)
        self.assertEqual(fibonacci(17), 1597)
        self.assertEqual(fibonacci(18), 2584)
        self.assertEqual(fibonacci(19), 4181)
        self.assertEqual(fibonacci(20), 6765)

    def test_fibonacci_large(self):
        self.assertEqual(fibonacci(30), 832040)
        self.assertEqual(fibonacci(40), 1027586592)
        self.assertEqual(fibonacci(50), 354224848179261915075)
        self.assertEqual(fibonacci(60), 2231785803678884676694200729369)
        self.assertEqual(fibonacci(70), 35421772801494944457777580742074788140197119384600368)
        self.assertEqual(fibonacci(80), 600851475143)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-2)
        with self.assertRaises(ValueError):
            fibonacci(-3)
        with self.assertRaises(ValueError):
            fibonacci(-4)
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_fibonacci_non_integer(self):
        with self.assertRaises(TypeError):
            fibonacci("abc")
        with self.assertRaises(TypeError):
            fibonacci([])
        with self.assertRaises(TypeError):
            fibonacci({"key": "value"})