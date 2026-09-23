def lex_insert(L, a, b):
    L.append((a, b))
    L.sort()
    #return the list in lexicographic order
    return L
#example usage of the function
L = [(1, 10), (3, 1), (0, 9)]
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
print(lex_insert(L, a, b))


