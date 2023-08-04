# Factorial Digit Sum
# Find the sum of the digits in the number 100!

number_to_test = 100


def get_factorial(n):
    """ Given a number, compute the factorial of that number. """
    if n <= 1:
        return 1
    else:
        return n * get_factorial(n - 1)


def get_digit(num, n):
    """ Gets the Nth digit of a number. """
    return num // 10**n % 10


def find_digit_sum(num):
    """ Returns the sum of a given number's digits. """
    digits = []
    for i in range(len(str(num))):
        current_digit = get_digit(num, i)
        digits.append(current_digit)
    return sum(digits)


print("The sum of the digits in " + str(number_to_test) + "! is " + str(find_digit_sum(get_factorial(number_to_test))))
