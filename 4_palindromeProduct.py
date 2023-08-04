# Largest palindrome product
# Find the largest palindrome made from the product of two 3-digit numbers


# Creates a list of palindromes formed by two 3-digit numbers
def get_max_palindrome():
    palindromes = []
    for i in range(100, 999):
        for j in range(100, 999):
            candidate = j * i
            if check_if_palindrome(candidate):
                palindromes.append(candidate)
    return max(palindromes)


# Checks if a number is a palindrome or not by putting each digit into a list and checking if the beginning of the list equals the end until you reach the middle
def check_if_palindrome(num):
    digits = [int(x) for x in str(num)]
    for i in range(0, len(digits)):
        if digits[i] == digits[0 - (i + 1)]:
            continue
        else:
            return False
    return True


print(get_max_palindrome())
