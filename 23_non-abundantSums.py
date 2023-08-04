# Non-Abundant Sums
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math
import time

start_time = time.time()
stop_condition = 28123


def get_proper_divisors(num):
    """ Gets all proper divisors for a given number and returns a list of proper divisors. """
    proper_divisors = [1]
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0 and i < num:
            proper_divisors.extend([i, num // i])
    return list(set(proper_divisors))


def check_if_abundant(num):
    """ Checks whether a given number is abundant or not.  An abundant number, n, is a number where the sum of proper divisors it greater than n. """
    return sum(get_proper_divisors(num)) > num


def get_abundant_nums(limit):
    """ Gets all abundant numbers up to a given limit.  Returns a list of abundant numbers. """
    abundant_nums = []
    for nums in range(1, limit + 1):
        abundant_nums.append(check_if_abundant(nums))
    return abundant_nums


def non_abundant_sum(limit):
    """ Returns the sum of all positive integers that cannot be written as the sum of two abundant numbers. """
    abundant_nums = get_abundant_nums(limit)

    not_sum_of_abundants = 0

    # the number, n, is what we will be checking
    for n in range(1, len(abundant_nums)):
        are_abundant = False
        # compare n's divisors to check if there are two abundant numbers among them
        for i in range(1, math.ceil(n // 2) + 1):
            # if there are two abundant numbers then break the loop and go to the next number
            if abundant_nums[i - 1] and abundant_nums[(n - i) - 1]:
                are_abundant = True
                break
        # if the current number, n, can not summed from two abundant numbers then add it to the total
        if not are_abundant:
            not_sum_of_abundants += n
    return not_sum_of_abundants


print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is: " + str(non_abundant_sum(stop_condition)))
print("--- %s seconds ---" % "{:.2f}".format((time.time() - start_time)))
