# Fibonacci Sequence
# Find the sum of even-valued numbers of the fibonacci sequence that don't exceed 4 million

fibFirst = 0  # First number in fib sequence
fibSecond = 1  # Second number in fib sequence
listFib = [fibFirst]  # list of the fibonacci sequence (currently only the first number is saved)
limit = 4000000  # limit you want to sum to


# Fibonacci Sequence Formula: N = N_n-1 + N_n-2
def fibonacci_sequence(nMinusOne, nMinusTwo):
    nextNum = nMinusOne + nMinusTwo

    # Save the number to a list if it is even
    if nextNum % 2 == 0:
        listFib.append(nextNum)
    if nextNum > limit:
        return 0
    else:
        return fibonacci_sequence(nextNum, nMinusOne)


# Sum all numbers in a list
def find_sum(lst):
    total = 0
    for i in range(0, len(lst)):
        total += lst[i]
    return total


fibonacci_sequence(fibFirst, fibSecond)
print("The sum of the even numbers in the fibonacci sequence that don't exceed 4 million is: " + str(find_sum(listFib)))
