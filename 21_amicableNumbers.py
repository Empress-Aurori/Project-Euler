# Amicable Numbers
# Evaluate the sum of all the amicable numbers under 10000.

import math
import time

start_time = time.time()
stopping_point = 10000


def get_proper_divisors(num):
    """ Gets all proper divisors for a given number and returns a list of proper divisors. """
    proper_divisors = [1]
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0 and i < num:
            proper_divisors.extend([i, num // i])
    return list(set(proper_divisors))


def get_sum(lst):
    """ Gets the sum of a list of numbers. """
    return sum(lst)


def check_if_amicable(a, b):
    """ Checks whether numbers a and b are amicable.  This will return True if they are, and return False if they aren't. """
    if b > a != b and get_sum(get_proper_divisors(b)) == a:
        return True
    else:
        return False


def sum_amicable_numbers(limit):
    """ Returns the sum of all amicable numbers under a given limit. """
    amicable_numbers = []
    a = 1
    for i in range(1, limit):
        b = get_sum(get_proper_divisors(a))
        if check_if_amicable(a, b):
            amicable_numbers.append(a)
            amicable_numbers.append(b)
        a += 1

    return get_sum(amicable_numbers)


print("The sum of all amicable numbers under " + str(stopping_point) + " is: " + str(
    sum_amicable_numbers(stopping_point)))
print("--- %s seconds ---" % "{:.2f}".format((time.time() - start_time)))
