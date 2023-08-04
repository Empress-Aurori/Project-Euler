# Digit Fifth Powers
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import time

start_time = time.time()
max_search = 200000


def get_digit(num, n):
    """ Gets the Nth digit of a number. """
    return num // 10**n % 10


def fifth_power_sum(limit):
    """ Returns the sum of all the numbers that can be written as the sum of fifth powers of their digits. """
    n = 10
    power_sum = 0
    sum_digits = 0
    while n <= limit:
        for digit in range(len(str(n))):
            sum_digits += get_digit(n, digit)**5
        if sum_digits == n:
            power_sum += n
        sum_digits = 0
        n += 1
    return power_sum


print("The sum of all numbers that can be written as the sum of fifth powers of their digits is " + str(fifth_power_sum(max_search)))
print("--- %s seconds ---" % "{:.2f}".format((time.time() - start_time)))
