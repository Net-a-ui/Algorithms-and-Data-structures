#Goal take a string and put its reverse after it

def palindrome(txt):
    return txt + txt[::-1]

#example usage of the function
txt = input("Enter a string: ")
print(palindrome(txt))

