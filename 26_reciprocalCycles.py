# Reciprocal Cycles
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# Explanation for formula used: https://softwareengineering.stackexchange.com/questions/192070/what-is-a-efficient-way-to-find-repeating-decimal
# Code for finding a repeating string in a decimal: http://codepad.org/hKboFPd2

import time

start_time = time.time()
stop_condition = 1000


def find_longest_cycle(limit):
    """ Returns the value of the denominator that yields the longest recurring decimal cycle for d < limit for the unit fraction 1/d. """
    # initial conditions
    d = 2
    longest_denominator = d
    biggest_cycle_length = 0

    while d < limit:
        c = 10 * (1 % d)
        digits = ""
        passed = {}
        i = 0
        while True:
            # if we find a duplicate power of 10 remainder
            if c in passed:
                cycle = digits[passed[c]:]  # amount of digits in the cycle
                if cycle == '0':
                    current_cycle_length = 0
                else:
                    current_cycle_length = len(cycle)
                break
            current_digit = c // d  # finds the digits after the decimal
            remainder = c % d
            passed[c] = i
            digits += str(current_digit)
            i += 1
            c = 10 * remainder
        if current_cycle_length > biggest_cycle_length:
            longest_denominator = d
            biggest_cycle_length = current_cycle_length
        d += 1
    return longest_denominator


print("The value of the denominator that produces the largest recurring cycle for d < " + str(stop_condition) + " in the 1/d relation is " + str(find_longest_cycle(stop_condition)))
print("--- %s seconds ---" % "{:.2f}".format((time.time() - start_time)))
