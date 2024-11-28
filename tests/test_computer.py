import unittest
from computer import add, subtract, multiply, divide

class TestComputer(unittest.TestCase):
    # Test for addition
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    # Test for subtraction
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 1), -1)
        self.assertEqual(subtract(-1, -1), 0)

    # Test for multiplication
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    # Test for division
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(3, 1), 3)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()


