#a static list of "apple", "banana", and "peach" is printed
print(["apple","banana","peach"])

#prints a list from 0 to 7
list = range(8)
print(list)

#prints a list from 2 to 24
list = range(2,25)
print(list)

#appends to an empty list to create the desired outcome and prints it
#in this case, create a list of squares from 0 to 9
square = []
for x in range(10):
	square.append(x**2)
print(square)

#this can be more succintly done with:
square = [x**2 for x in range(10)]
print(square)
