# Distinct Powers
# How many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100?

import time

start_time = time.time()


def get_sequence_length():
    power_sequence = set()
    a = 2
    while a <= 100:
        for b in range(2, 101):
            power_sequence.add(a**b)
        a += 1
    return len(power_sequence)


print("There are " + str(get_sequence_length()) + " distinct terms in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100.")
print("--- %s seconds ---" % "{:.2f}".format((time.time() - start_time)))