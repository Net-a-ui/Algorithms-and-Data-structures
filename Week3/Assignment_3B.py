# Juvenal Nava
# Programming Assignment 3B

'''
This program accepts two positive integers
and uses recursion to find the Greatest Common Divisor.
'''

def gcd(number1, number2):

    # base case
    if number2 == 0:
        return number1

    # recursive case
    return gcd(number2, number1 % number2)

number1 = int(input("Enter the first positive integer: "))
number2 = int(input("Enter the second positive integer: "))

print("Greatest common divisor:", gcd(number1, number2))
