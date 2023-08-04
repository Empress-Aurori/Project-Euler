# Smallest Multiple
# Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

# Loop through all of the multiples of 20 that are greater than 1000 and stop if the number is divisible by 1 through 20
def smallest_divisor():
    i = 1000
    while True:
        if is_divisible(i):
            break
        i += 20
    return i


# Check if a number, n, is divisible by numbers 2 through 20 (redundant to check if divisible by 1)
def is_divisible(n):
    for i in range(2, 20):
        if n % i == 0:
            continue
        else:
            return False
    return True


print(smallest_divisor())
