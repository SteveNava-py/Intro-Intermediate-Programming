# Name: Steven Marco Navarrette
# solution a: dictionary comprehension to create dictionary
cube_dict = {x: x * x * x for x in range(1, 6)}

# solution b: method that mimics dictionary and dictionary comprehension
def new_cube_dic():
    cube_dic = {}
    for x in range(1, 6):  # uses for loop that adds the integer passed through it but cubed from 1 to 5
        cube_dic[x] = x * x * x
    return cube_dic


# solution b: invokes function and creates dictionary
cube_dic = new_cube_dic()

print(cube_dic)
print(cube_dict)

# expected result should be dictionary with keys being 1 to 6 and their values being cubed
