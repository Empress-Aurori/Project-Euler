# Displays the sum of multiples of 2 numbers up to a specified limit

increment1 = 3
increment2 = 5
testLimit = 1000


# Get all of the multiples of a number up to a certain limit and return the sum of all the numbers gathered
def multiples(num, limit):
    multiple = 0
    sumNumbers = 0
    listMultiples = []
    for n in range(num, limit, num):
        multiple += num
        listMultiples.append(multiple)
    for n in range(0, len(listMultiples)):
        sumNumbers += listMultiples[n]
    return sumNumbers


# Get all of the shared multiples of 2 numbers up to a certain limit and sum all of the numbers gathered
def multiple_of_both(num1, num2, limit):
    multiple = 0
    sumNumbers = 0
    listMultiples = []
    for n in range(num1, limit, num1):
        multiple += num1
        if multiple % num2 == 0:
            listMultiples.append(multiple)
    for n in range(0, len(listMultiples)):
        sumNumbers += listMultiples[n]
    return sumNumbers


# test statements
total = multiples(increment1, testLimit) + multiples(increment2, testLimit) - multiple_of_both(increment1, increment2, testLimit)
print("The sum is: " + str(multiples(increment1, testLimit)) + ", for multiples of " + str(increment1))
print("The sum is: " + str(multiples(increment2, testLimit)) + ", for multiples of " + str(increment2))
print("\nThe sum of multiples of " + str(increment1) + " or " + str(increment2) + " up to " + str(testLimit) + " is: " + str(total))
