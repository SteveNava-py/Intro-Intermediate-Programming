# Name: Steven Marco Navarrette
# Define odd checking function
def odd_check(x):
    return x % 2 != 0  # utilizes modulus to check if odd in each iteration


# define method to square the numbers
def square_nums(x):
    return x * x  # squares each iteration of the list


# solution a: filters numbers 1 to 10 passed through odd check method
odd_numbers = filter(odd_check, range(1, 1001))

# maps the filtered numbers that are passed through square nums method
square_odd_nums = map(square_nums, odd_numbers)

# summates the filtered and mapped squared odd numbers
sum_square_odd_nums = sum(square_odd_nums)

# solution b: set the new sum equal to zero
sum_square_odd_nums_2 = 0

# utilize for loop to iterate from 1 to 1000 then if statement to check if number is odd then square it
for x in range(1, 1001):
    if x % 2 != 0:
        square_odd_nums_2 += x * x

print(sum_square_odd_nums)
print(sum_square_odd_nums_2)

# expected result should be a number in the 100 mils
