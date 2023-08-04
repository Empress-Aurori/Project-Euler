# Longest Collatz Sequence
# Which starting number, under one million, produces the longest chain in the Collatz Sequence?

import time

start_time = time.time()
start_limit = 1000000


def get_number_with_max_chain_length(limit):
    sequence = []
    max_length = 0
    max_start = 0
    for i in range(2, limit):
        current_start = i
        next_num = current_start
        sequence.append(next_num)

        while next_num != 1:
            if next_num % 2 == 0:
                next_num = next_num // 2
            else:
                next_num = (3 * next_num) + 1
            sequence.append(next_num)

        current_length = len(sequence)
        if current_length > max_length:
            max_start = current_start
            max_length = current_length
        sequence = []

    return max_start, max_length


print("The number, x, that produces the longest chain of length y is (x, y): " + str(get_number_with_max_chain_length(start_limit)))
print("--- %s seconds ---" % "{:.2f}".format((time.time() - start_time)))
