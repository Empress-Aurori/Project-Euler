# Self Powers
# Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000

limit = 1000


def get_digit(num, n):
    """ Gets the Nth digit of a number. """
    return num // 10**n % 10


def power_series(n):
    """ Finds the last ten digits of the power series 1^1 + 2^2 + 3^3 + ... n^n """
    sum_series = 0
    for i in range(1, n + 1):
        sum_series += i**i

    digits = [int(x) for x in str(sum_series)]
    return digits[-10:]


print("The last ten digits of the power series 1^1 + 2^2 + 3^3 + ... + " + str(limit) + "^" + str(limit) + " is: " + str(power_series(limit)))
