#basic input - in 2.7 raw_input does not evaluate the answer as a python statement
person = raw_input('Please enter your name: ')
print('Hello '+person)

#input evals as a Python expression - this will solve the given input and print that solution
answer = input("Enter an equation: ")
print(answer)

#reads a list of dynamic input and prints it
dynam = []
num_items = int(raw_input("How many items are in this list? "))
for x in range(num_items):
	item = raw_input("What is item number " + str(x)+ "? ")
	dynam.append(item)
print(list)

#creating a list from file input
f = open('input.txt','r') #r means read only
stuff = list(f)
#for line in list(f):
#	list.append(line)
print(stuff)
