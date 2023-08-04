# Sum Square Difference
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

limit = 100  # limit you want to sum to


# Get sum of squares of the first 100 natural numbers (1^2 + 2^2 + 3^2 + ... + 100^2 = [sumOfSquares]
def sum_of_squares(maximum):
    num = 0
    for n in range(1, maximum + 1):
        num += n**2
    return num


# Get the square of the sum of the first 100 numbers ( (1 + 2 + 3 + ... + 100)^2 = [squareOfSums]
def square_of_sums(maximum):
    num = 0
    for n in range(1, maximum + 1):
        num += n
    num = num**2
    return num


# Get the difference between the sum of squares and the square of sums ( [squareOfSums] - [sumOfSquares] )
print(square_of_sums(limit) - sum_of_squares(limit))
