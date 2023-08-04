# Special Pythagorean Triplet
# There exists one pythagorean triplet for which a + b + c = 1000.  Find the product abc.
# CONDITION 1: a < b < c
# CONDITION 2: a + b + c = 1000

limit = 700


def get_pythagorean_triplets(limits):
    c, m = 0, 2
    t = 0
    while c < limits:
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            t = t + 1
            product = a * b * c
            print(t, ")", a, b, c, " = ", a + b + c)
            print("The product of", a, b, c, "is", product)
            if c > limits:
                break
        m = m + 1


get_pythagorean_triplets(limit)
