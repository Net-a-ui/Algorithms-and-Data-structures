def balanced(txt):
    stack = [] # empty list will work as the stack
    for char in txt:
        # save every opening parenthesis in the stack
        if char == '(': 
            stack.append(char)
        # check every closing parenthesis against the stack
        elif char == ')': 
            #nothing in the stack to match the closing parenthesis
            if len(stack) == 0:
                return False
    return len(stack) == 0
#get expression from the user and show result(a)
txt = input("Enter an expression: ")
print("Balanced:", balanced(txt))

