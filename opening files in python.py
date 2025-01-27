f = open("testFile.txt", 'r')
line = f.read()
print(line)
print(type(line))


# you can for loop it

# for l in f:
# print(l, end=' ')

# you can use readlines() function

# f = open("testFile.txt", 'r')
# line2 = f.readline()
# print(line2)

# you can use the write() and close() function to create a text file
# f1 = open('file1.txt', "w")
# f1.write("Sonic: What the heck is ligma? ")
# f1.write("Sugma dik")
# f1.close()
