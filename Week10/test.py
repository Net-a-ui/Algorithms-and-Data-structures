table = [none] * 20
last = -1

table[0] = 3
table[1] = 21
table[3] = 6
last = 2
def isFull():
    return last == len(table) - 1

def isEmpty():
    return last == -1

#Using python, write function that removes the first item in the list.
#if the list not empty
def removeFirst():
    global last
    if not isEmpty():
        for i in range(1, last + 1):
            table[i - 1] = table[i]
        table[last] = None
        last -= 1

# using python, write function that inserts an item at the given index location, only if the list index location is not empty
def insertAt(index, item):
    global last
    if 0 <= index <= last:
        if not isFull():
            for i in range(last, index - 1, -1):
                table[i + 1] = table[i]
            table[index] = item
            last += 1
#using python, write a function finds and returns the location of the largest  value
def findLargest():
    if isEmpty():
        return -1
    max_index = 0
    for i in range(1, last + 1):
        if table[i] > table[max_index]:
            max_index = i
    return max_index

#using python, writ
#using python, write a function that prints only the first half of the list
def printFirstHalf():
    if isEmpty():
        return
    end = (last + 1) // 2
    for i in range(0, end):
        print(table[i])
##using python, write a function that prints only the first half of the list
def printFirstHalf():
    if isEmpty():
        return
    end = (last + 1) // 2
    for i in range(0, end):
        print(table[i])

#using python, write a function that updates (or adds) each item in the list by 2
def updateByTwo():
    if isEmpty():
        return
    for i in range(0, last + 1):
        table[i] += 2

#Using python, write a function that finds and returns the average value of all items in the list
def findAverage():
    if isEmpty():
        return 0
    total = 0
    for i in range(0, last + 1):
        total += table[i]
    return total / (last + 1)

#using python, write a function that finds and returns the difference between largest and smallest value in the list
def findDifference():
    if isEmpty():
        return 0
    max_val = table[0]
    min_val = table[0]
    for i in range(1, last + 1):
        if table[i] > max_val:
            max_val = table[i]
        if table[i] < min_val:
            min_val = table[i]
    return max_val - min_val
#using python, write a function that removes/deletes all the items in the list
def removeAll():
    global last
    for i in range(0, last + 1):
        table[i] = None
    last = -1