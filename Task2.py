# Name: Steven Marco Navarrette
# define the cube calculator function
def cube_cal(x):
    return x * x * x  # calculates the cube of each iteration


# solution a: list of numbers from 1 to 10 passed through the function, gets mapped, and is stored in the variable

nums = list(map(cube_cal, range(1, 11)))

# solution b: list comprehension instead of map function to pass numbers 1 to 10 through the same method

cubed_nums = [cube_cal(x) for x in range(1, 11)]

print(nums)
print(cubed_nums)

# expected result should be a list of numbers 1 to 10 cubed in each iteration
