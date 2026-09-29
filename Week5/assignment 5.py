#goal to make a program using backtracking to search thorugh possible combinations of numbers

def find_sum_indices(numbers, target):

    #backtracking function
    def backtrack(start, current, total):

        #if current sum reaches, return the indices
        if total == target:
            return current

        #if sumn goes over, stop this path
        if total > target:
            return[]

        for index in range(start, len(numbers)):

            #add current index to the list
            result = backtrack(index + 1, current + [index], total + numbers[index])

            #if solution was foud, it return it
            if result:
                return result

        #if no solution was found, return empty list
        return []

    return backtrack(0, [], 0)

#test uno
x = [3, 4, 7, 8]
target = 11
print(find_sum_indices(x, target))

#test dos
x = [2, 5, 9, 12]
target = 14
print(find_sum_indices(x, target))

#test tres
x = [1, 2, 3]
target = 10
print(find_sum_indices(x, target))
