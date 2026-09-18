# Juvenal Nava
# Programming Assignment 3A

'''
This program accepts a positive integer
and uses recursion to return its hexadecimal value.
'''

def decimal_to_hex(number):
    hex_digits = "0123456789ABCDEF"

    # base case
    if number < 16:
        return hex_digits[number]

    # recursive case
    return decimal_to_hex(number // 16) + hex_digits[number % 16]

number = int(input("Enter a positive integer: "))
print("Hexadecimal value:", decimal_to_hex(number))
