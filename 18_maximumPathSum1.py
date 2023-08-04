# Maximum Path Sum I
# Find the maximum total from top to bottom of the triangle below:
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

numbers = """
75 00 00 00 00 00 00 00 00 00 00 00 00 00 00
95 64 00 00 00 00 00 00 00 00 00 00 00 00 00
17 47 82 00 00 00 00 00 00 00 00 00 00 00 00
18 35 87 10 00 00 00 00 00 00 00 00 00 00 00
20 04 82 47 65 00 00 00 00 00 00 00 00 00 00
19 01 23 75 03 34 00 00 00 00 00 00 00 00 00
88 02 77 73 07 63 67 00 00 00 00 00 00 00 00
99 65 04 28 06 16 70 92 00 00 00 00 00 00 00
41 41 26 56 83 40 80 70 33 00 00 00 00 00 00
41 48 72 33 47 32 37 16 94 29 00 00 00 00 00
53 71 44 65 25 43 91 52 97 51 14 00 00 00 00
70 11 33 28 77 73 17 78 39 68 17 57 00 00 00
91 71 52 38 17 14 91 43 58 50 27 29 48 00 00
63 66 04 68 89 53 67 30 73 16 69 87 40 31 00
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def create_grid(string):
    """ Creates an [n x n] matrix of numbers from a given string.  Reference the grid as grid[y][x] or grid[row][column]. """
    # https://stackoverflow.com/questions/54701681/string-to-nn-matrix-in-python
    # Explanation in first response
    nums = string.split()
    n = int(len(nums) ** 0.5)  # length and width of the matrix

    # https://stackoverflow.com/questions/29139350/difference-between-ziplist-and-ziplist
    # zip(*[map(int, nums)] * n) explanation: the * symbol at the beginning of the statement unpacks the elements into separate arguments
    return list(map(list, zip(*[map(int, nums)] * n)))


def get_max_path_sum(triangle):
    """ Finds the max path sum of a given triangle starting from the 2nd to last row and returns the top of the triangle. """
    # starts at the 2nd to last row and moves up
    for row in range(len(triangle) - 2, -1, -1):
        # loops through each column of the given grid
        for column in range(len(triangle[row])):
            # ignore 0 in the grid
            if triangle[row][column] == 0:
                continue
            else:
                # looks at each number in the current row and gets the max path value of the row below it
                triangle[row][column] += max(triangle[row + 1][column], triangle[row + 1][column + 1])

    # once the loop is exited the top of the triangle will have the max path sum
    return triangle[0][0]


grid = create_grid(numbers)
print(get_max_path_sum(grid))
