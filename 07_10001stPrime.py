# 10001st Prime
# What is the 10,001st prime number?

# length of list
limit = 10001


def check_if_prime(n):
    """ Returns True or False depending on if the given n is prime. """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_primes(n):
    """ Gets all of the prime numbers up to a specified n and returns a list of prime numbers. """
    primes = []
    i = 3
    while True:
        if check_if_prime(i):
            primes.append(i)
        if len(primes) == n:
            break
        else:
            i += 2
    return primes


print(get_primes(limit))
