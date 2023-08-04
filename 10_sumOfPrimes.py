# Summation of Primes
# Find the sum of all the primes below 2 million

from itertools import compress

limit = 2000000
# primes = []


# Checks whether or not a number is prime
# def check_if_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


def sum_primes(max_limit):
    """ Returns the sum of all prime numbers below a given limit. """
    # print("Loading answer...")
    # for i in range(2, max_limit):
    #     if check_if_prime(i):
    #         primes.append(i)
    # summedPrimes = sum(primes)
    # return summedPrimes
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (max_limit // 2)
    for i in range(3, int(max_limit ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((max_limit - i * i - 1) // (2 * i) + 1)
    return sum([2, *compress(range(3, max_limit, 2), sieve[1:])])


print(sum_primes(limit))
