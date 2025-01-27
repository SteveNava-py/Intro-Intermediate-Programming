# Name: Steven Marco Navarrette
from functools import reduce


# solution a: method that finds the minimum number in list
def find_minimum(x, y):
    return min(x, y)


# solution b: method that find minimum without listed number being passed throuhg it
def find_min(x):
    if not x:
        return None
    min_val = x[0]
    for num in x[1:]:
        if num < min_val:
            min_val = num
        return min_val


# solution a: list of integers ranging from 1 to 5
numbers = list(range(1, 6))
min_value = reduce(find_minimum, numbers)

# solution b: using reduce function the passes the list through minimum function
min_val = find_min(numbers)

print(min_val)
print(min_value)

# expected result should be 1 for both solutions
