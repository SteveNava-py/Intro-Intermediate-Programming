# Name: Steven Marco Navarrette
# define the function div4
def div4(x):
    return x % 4 == 0  # check divisibility by four using modulus


# define the custom function
def custom_four_filter(first):
    return [x for x in first if x % 4 == 0]  # utilizes list comprehension that checks for multiples of four


# solution A using built-in function filter with div4 method

multiples_of_four_a = list(filter(div4, range(1, 101)))

# solution b creating new list without filter function

nums = list(range(1, 101))

# solution b calling the function and passing each number in the list through it and storing it in variable

multiples_of_four_b = custom_four_filter(nums)

print(multiples_of_four_a)
print(multiples_of_four_b)

# The expected result should be the multiples of four from 1 to 100
