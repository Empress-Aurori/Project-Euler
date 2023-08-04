# Lexicographic Permutations
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import time

start_time = time.time()
permutation_limit = 1000000


def get_factorial(n):
    """ Given a number, compute the factorial of that number. """
    if n <= 1:
        return 1
    else:
        return n * get_factorial(n - 1)


def get_kth_permutation(k_0):
    """ Gets the kth permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. """
    # formula origin: https://math.stackexchange.com/questions/60742/finding-the-n-th-lexicographic-permutation-of-a-string
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    k = k_0  # initial condition

    # k = (q * n!) + r
    for n in range(9, 0, -1):
        for q in range(len(digits), 0, -1):
            if (q * get_factorial(n)) < k:
                k = k - (q * get_factorial(n))  # k_next = r = k_current - q(n!)
                result.append(digits[q])
                digits.pop(q)  # pop = remove
                break
    result.append(digits[0])  # the only remaining digit should be 0, so add it to the end of the result

    return result


print("The " + str(permutation_limit) + "th permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 is " + str(get_kth_permutation(permutation_limit)))
print("--- %s seconds ---" % "{:.2f}".format((time.time() - start_time)))
