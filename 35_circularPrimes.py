# Circular Primes
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# How many circular primes are there below one million?

# function to get a prime number
# function to get all the digits of a number
# function to check if each order of the digits of a number is prime

upper_limit = 100


def get_circular_primes(limit):
    """ Returns a list of all prime numbers up to the given limit. """

    circular_primes = 0
    for n in range(2, limit+1):
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            get_digits(n)
    return circular_primes


def check_if_prime(n):
    """ Returns True if n is prime, False otherwise. """

    if n < 2:  # 0 and 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_digits(n):
    """ Returns a list of all the digits of the given number. """

    digits = []
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10
    digits.reverse()
    return digits
