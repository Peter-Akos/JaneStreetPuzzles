import unittest


def square(num):
    # Checks if the input is a square number
    return num == int(num ** 0.5) ** 2


def palindrome(num):
    # Checks if the input is a palindrome number
    return str(num) == str(num)[::-1]


def one_more_than_palindrome(num):
    # Checks if the input is one more than a palindrome number
    return palindrome(num - 1)


def one_less_than_palindrome(num):
    # Checks if the input is one less than a palindrome number
    return palindrome(num + 1)


def prime_raised_to_prime_power(num):
    # Checks if the input is a prime number raised to a prime power
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return prime(num)


def prime(num):
    # Checks if the input is a prime number
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sum_of_digits_is_7(num):
    # Checks if the sum of the digits of the input is 7
    return sum(map(int, str(num))) == 7


def fibonacci(num):
    # Checks if the input is a Fibonacci number
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num


def multiple_of_37(num):
    # Checks if the input is a multiple of 37
    return num % 37 == 0


def palindrome_multiple_of_23(num):
    # Checks if the input is a palindrome number that is a multiple of 23
    return palindrome(num) and num % 23 == 0


def product_of_digits_ends_in_1(num):
    # Checks if the product of the digits of the input ends in 1
    product = 1
    for digit in str(num):
        product *= int(digit)
    return product % 10 == 1


def multiple_of_88(num):
    # Checks if the input is a multiple of 88
    return num % 88 == 0


def power_of_7(num):
    # Checks if the input is a power of 7
    if num < 1:
        return False
    while num % 7 == 0:
        num /= 7
    return num == 1


def multiple_of_5(num):
    # Checks if the input is a multiple of 5
    return num % 5 == 0


def cube(num):
    # Checks if the input is a cube number
    return num == int(num ** (1 / 3)) ** 3


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
        self.assertFalse(cube(9))


if __name__ == '__main__':
    unittest.main()
