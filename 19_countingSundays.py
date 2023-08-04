# Counting Sundays
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import time
import math

start_time = time.time()

day_to_check = 1  # what day of the month do you want to check
starting_year = 1901  # what year you want to start with
ending_year = starting_year + 100  # ends a century after the starting year


def get_sundays(day, current_year, end_year):
    """ Returns how many sundays land on the Nth day of the month. """
    # https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html for the equation used to get the week_day
    sunday_count = 0

    while current_year < end_year:
        century = int(str(current_year)[:2])
        for month in range(1, 12 + 1):
            week_day = (day + math.floor((2.6 * month) - 0.2) - (2 * century) + abs(current_year) % 100 + math.floor(abs(current_year) % 100 // 4) + math.floor(century // 4)) % 7
            if week_day == 0:
                sunday_count += 1
        current_year += 1

    return sunday_count


print("There are " + str(get_sundays(day_to_check, starting_year, ending_year)) +
      " Sundays that land on the " + str(day_to_check) + " of the month during the time period of " +
      str(starting_year) + " to " + str(ending_year))
print("--- %s seconds ---" % "{:.2f}".format((time.time() - start_time)))
