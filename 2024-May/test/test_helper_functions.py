import unittest
from src.helper_functions import square, palindrome, one_more_than_palindrome, one_less_than_palindrome, \
    prime_raised_to_prime_power, prime, sum_of_digits_is_7, fibonacci, multiple_of_37, palindrome_multiple_of_23, \
    product_of_digits_ends_in_1, multiple_of_88, power_of_7, multiple_of_5, cube


class TestHelperFunctions(unittest.TestCase):

    def test_square(self):
        self.assertTrue(square(4))
        self.assertFalse(square(3))

    def test_palindrome(self):
        self.assertTrue(palindrome(121))
        self.assertFalse(palindrome(123))

    def test_one_more_than_palindrome(self):
        self.assertTrue(one_more_than_palindrome(122))
        self.assertFalse(one_more_than_palindrome(123))

    def test_one_less_than_palindrome(self):
        self.assertTrue(one_less_than_palindrome(120))
        self.assertFalse(one_less_than_palindrome(123))

    def test_prime_raised_to_prime_power(self):
        self.assertTrue(prime_raised_to_prime_power(2))
        self.assertFalse(prime_raised_to_prime_power(4))

    def test_prime(self):
        self.assertTrue(prime(7))
        self.assertFalse(prime(8))

    def test_sum_of_digits_is_7(self):
        self.assertTrue(sum_of_digits_is_7(16))
        self.assertFalse(sum_of_digits_is_7(15))

    def test_fibonacci(self):
        self.assertTrue(fibonacci(5))
        self.assertFalse(fibonacci(4))

    def test_multiple_of_37(self):
        self.assertTrue(multiple_of_37(74))
        self.assertFalse(multiple_of_37(75))

    def test_palindrome_multiple_of_23(self):
        self.assertFalse(palindrome_multiple_of_23(25352))
        self.assertFalse(palindrome_multiple_of_23(25353))

    def test_product_of_digits_ends_in_1(self):
        self.assertTrue(product_of_digits_ends_in_1(1111111))
        self.assertFalse(product_of_digits_ends_in_1(22))

    def test_multiple_of_88(self):
        self.assertTrue(multiple_of_88(176))
        self.assertFalse(multiple_of_88(177))

    def test_power_of_7(self):
        self.assertTrue(power_of_7(49))
        self.assertFalse(power_of_7(50))

    def test_multiple_of_5(self):
        self.assertTrue(multiple_of_5(10))
        self.assertFalse(multiple_of_5(11))

    def test_cube(self):
        self.assertTrue(cube(8))
        self.assertTrue(cube(3375))
        self.assertFalse(cube(9))
        self.assertTrue(cube(1))  # 1^3 = 1
        self.assertTrue(cube(0))  # 0^3 = 0
        self.assertTrue(cube(-27))  # (-3)^3 = -27
        self.assertTrue(cube(64))  # 4^3 = 64
        self.assertTrue(cube(-125))  # (-5)^3 = -125
        self.assertTrue(cube(125))  # 5^3 = 125
        self.assertFalse(cube(2))  # 2 is not a perfect cube
        self.assertFalse(cube(50))  # 50 is not a perfect cube
        self.assertFalse(cube(-16))  # -16 is not a perfect cube
        self.assertTrue(cube(729))  # 9^3 = 729
        self.assertFalse(cube(1000.1))  # 1000.1 is not a perfect cube
        self.assertTrue(cube(-1))  # (-1)^3 = -1
