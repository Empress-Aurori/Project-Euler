# Number Spiral Diagonals
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?

import math

grid_size = 1001  # size n of an nxn grid


def sum_grid_diagonals(grid_length):
    """ Will return the sum of the diagonals of an nxn grid formed by starting from 1 and moving to the right in a clockwise direction to form a spiral of numbers. """
    a_0 = 1  # first term in the series
    n = 1  # nth index of the series, starting from n = 1 (the 2nd term in the series)
    prev_term = a_0
    next_term = 0
    last_term = grid_length ** 2
    total = 0
    while next_term < last_term:
        next_term = prev_term + 2 * (math.ceil(n / 4))  # S_n = a_n-1 + ( 2 * ceil( n / 4 ) )
        total += next_term
        prev_term = next_term
        n += 1
    return a_0 + total


print("The sum of the diagonals of a " +
      str(grid_size) + "x" + str(grid_size) +
      " grid formed by starting from 1 and moving to the right and in a clockwise direction is " +
      str(sum_grid_diagonals(grid_size)))
