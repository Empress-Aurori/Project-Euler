# Highly Divisible Triangular Number
# What is the value of the first triangle number to have over 500 divisors?

import time
import math

start_time = time.time()
divisor_limit = 500


def get_triangular_numbers():
    """ Returns the triangular number with over a specified amount of factors. """
    num = 0
    index = 1
    while True:
        num += index
        index += 1
        yield num


def get_factors(num):
    """ Returns the amount of factors a number has. """
    factor_count = 0
    for i in range(1, round(math.sqrt(num))):
        if num % i == 0:
            factor_count += 2
    if round(math.sqrt(num)) * round(math.sqrt(num)) == num:
        factor_count += 1
    return factor_count


def get_value(limit):
    """ Returns the triangular number with the greatest amount of factors. """
    for triangularNumber in get_triangular_numbers():
        factor_total = get_factors(triangularNumber)
        if factor_total > limit:
            return triangularNumber


print("The value of the first triangular number with over " + str(divisor_limit) + " divisors is: " + str(get_value(divisor_limit)))
print("--- %s seconds ---" % "{:.2f}".format((time.time() - start_time)))
