# Number Letter Counts
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

from functools import reduce

limit = 1000

teens = {
    0: "ten",
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen"
}

# number: [ones place, tens place, hundreds place, thousands place]
digits_as_words = {
    0: ["", "", ""],
    1: ["one", "ten", "onehundred", "onethousand"],
    2: ["two", "twenty", "twohundred"],
    3: ["three", "thirty", "threehundred"],
    4: ["four", "forty", "fourhundred"],
    5: ["five", "fifty", "fivehundred"],
    6: ["six", "sixty", "sixhundred"],
    7: ["seven", "seventy", "sevenhundred"],
    8: ["eight", "eighty", "eighthundred"],
    9: ["nine", "ninety", "ninehundred"],
}


def get_digit(num, n):
    """ Gets the Nth digit of a number. """
    return num // 10**n % 10


def number_to_word(num):
    """ Converts a given number into its word equivalent. """
    number_as_word = []
    digits = 0

    # loop through each digit and use the digit as a key from the "digits_as_words" dictionary
    for i in range(len(str(num))):
        current_digit = get_digit(num, i)
        digits += 1
        if i == 1 and current_digit == 1:
            number_as_word.clear()
            number_as_word.append(teens[get_digit(num, 0)])
        else:
            number_as_word.append(digits_as_words[current_digit][i])

    # if we have more than 3 digits then we are in the hundreds place, so add an 'and' after the hundreds place for proper wording
    if (get_digit(num, 0) != 0 or get_digit(num, 1) != 0) and digits >= 3:
        number_as_word.insert(len(number_as_word) - 1, "and")
    number_string = ''.join(map(str, reversed(number_as_word)))

    return number_string


def sum_letters(n):
    """ Gets the amount of letters for numbers (as words) 1 to N """
    return reduce(lambda a, b: a + len(number_to_word(b)), range(1, n + 1), 0)


print("It takes " + str(sum_letters(limit)) + " letters to write out the numbers 1 to " + str(limit) + " in words.")
