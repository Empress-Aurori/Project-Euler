# Power Digit Sum
# What is the sum of the digits of the number 2^1000?

index = 1000


def power_digit_sum(exp):
    power = 2**exp
    digits = list(map(int, f"{power}"))
    return sum(digits)


print("The sum of the digits of 2^" + str(index) + " is: " + str(power_digit_sum(index)))
