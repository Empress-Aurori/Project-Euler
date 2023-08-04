# 1000-digit Fibonacci Number
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

limit = 1000  # stop the program when you exceed stop_digits digits


def n_digit_fibonacci_index(n):
    """ Gets all of the numbers in the fibonacci sequence that have less than a given limit of digits and returns the index of the last item in the list. """
    # Fibonacci Sequence Formula: N = N-1 + N-2
    fib_sequence = [0, 1, 1]
    while len(str(fib_sequence[-1])) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return len(fib_sequence) - 1


print("The index of the first term in the fibonacci sequence to contain 1000 digits is " + str(n_digit_fibonacci_index(limit)))
