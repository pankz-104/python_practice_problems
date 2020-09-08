# Palindrome
# A palindrome is a string which when reversed is itself.
# Example :: mom, 1221, 1000001
#
#     you have to take number as an input from user . you have to find the next
# palindrome corresponding to that number. Your input should be number of test cases
# and then take all the test cases from the user
#
# Input :
# 3
# 345
# 1221
# 451
#
# output :
# next palindrome for 3 is 4
# next palindrome for 345 is 343
# next palindrome for 451 is 454
#

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n = n + 1
    while not is_palindrome(n):
        n += 1
    return n

if __name__ == '__main__':
    n = int(input("Enter the number of test cases\n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number: \n"))
        numbers.append(number)

    for i in range(n):
        print(f"next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
