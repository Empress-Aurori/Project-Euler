# Names Scores
# 1) Sort the names in the file 22_names.txt in alphabetical order.
# 2) Then get the alphabetical value for each name.
# Alphabetical Value: get the position of each letter in a name, then the sum of those positions is the alphabetical value
# 3) Multiply the alphabetical value by the alphabetical position in the list.  This will be the name score for that name.
# What is the total of all the name scores in the file?

def get_names():
    """ Gets the contents of a given file and returns an alphabetically sorted list of the file's contents. """
    names_file = open("22_names.txt")
    read_data = names_file.read()
    read_data = read_data.replace("\"", "")
    names = read_data.split(",")
    names_file.close()
    names.sort()
    return names


def get_alphabetical_values(lst):
    """ Given a name, return the alphabetical_value """
    values = []
    for name in range(len(lst)):
        alphabetical_value = 0
        for char in lst[name].lower():
            alphabetical_value += (ord(char) - 96)
        values.append(alphabetical_value)

    return values


def get_total_name_score(value_list):
    """ Given a list of alphabetical_values, multiplies the values by the position the given name is in the list and returns the total_name_score """
    total_name_score = 0
    for value in range(len(value_list)):
        current_name_score = (value + 1) * value_list[value]
        total_name_score += current_name_score
    return total_name_score


names_list = get_names()
print("The total names score for the names in the 22_names.txt file is " + str(get_total_name_score(get_alphabetical_values(names_list))))
