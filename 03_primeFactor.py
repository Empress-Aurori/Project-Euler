# Largest Prime Factor
# What is the largest prime factor of the number 600851475143

# See https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python for explanation on line (21)

# Number you are testing
testNumber = 600851475143


# Checks whether a number is prime
def check_if_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Gets the largest prime factor of a number
def find_largest_prime_factor(n):
    factors = set([])
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and check_if_prime(i):
            factors.add(i)
    return max(factors)


# test statement
print("The largest prime factor for " + str(testNumber) + " is: " + str(find_largest_prime_factor(testNumber)))
