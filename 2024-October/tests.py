import unittest
from finder import apply_operations


class MyTestCase(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(apply_operations('aaa', 2, 3, 5), 6)  # 2 + 2 + 2

    def test_mixed_operations(self):
        self.assertEqual(apply_operations('aabcbc', 2, 3, 5), 900)  # 2 + 2 * 3 * 5 * 3 * 5

    def test_alternating_characters(self):
        self.assertEqual(apply_operations('abcabc', 1, 2, 3), 36)  # 1 * 2 * 3 * 1 * 2 * 3

    def test_single_character(self):
        self.assertEqual(apply_operations('c', 7, 11, 13), 13)  # Just 'c', so 13

    def test_only_additions(self):
        self.assertEqual(apply_operations('bbbb', 10, 20, 30), 80)  # 20 + 20 + 20 + 20

    def test_only_multiplications(self):
        self.assertEqual(apply_operations('abc', 2, 3, 5), 30)  # 2 * 3 * 5

    def test_large_values(self):
        self.assertEqual(apply_operations('a', 1000, 2000, 3000), 1000)  # Single 'a', so 1000

    def test_mixed_add_and_multiply(self):
        self.assertEqual(apply_operations('abac', 1, 5, 10), 50)  # 1 * 5 * 1 * 10

    def test_large_input_string(self):
        self.assertEqual(apply_operations('a' * 10 + 'b' * 5 + 'c' * 3, 2, 3, 4), 296)  # Complex case

    def test_zero_values(self):
        self.assertEqual(apply_operations('abc', 0, 3, 5), 0)  # First value is 0, result is 0


if __name__ == '__main__':
    unittest.main()