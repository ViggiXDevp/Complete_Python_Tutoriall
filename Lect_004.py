# =========== Lists & it's functions ==========

mylist = ["Ironman", "Thor", "Captain America", "Hulk", "Black Widow", "Hawkeye", 3000]

print(mylist[5])           # Prints the content present at index 5 i.e; "Hawkeye"

numbers = [2, 8, 9, 11, 69, 7]

print(numbers[4])          # Prints the content present at index 4 i.e; 69
print(numbers[1:4])        # Prints the contents of list from index 1 and goes upto index 3...(index 4 not counts)

# Maximum and Minimum values of List
print(max(numbers))        # Prints the maximum value of the list
print(min(numbers))        # Prints the minimum value of the list

# Functions to arrange the contents of the list
numbers.sort()             # The sort function is used to arrange the list elements in ascending order
print(numbers)
numbers.reverse()          # The reverse function is used to reverse the elements of the list
print(numbers)


# Function to add numbers in the list
numbers.append(7)          # The append function is used to add any string or other data type in the list
numbers.append('vighnesh')
numbers.append('1995')
print(numbers)


# Function to add element at specified index
numbers.insert(1, 54)      # list.insert(index no , element) Adding element at given index
numbers.insert(2, 74)
numbers.insert(3, 78)
print(numbers)


# Function to delete element at given index
numbers.pop(3)             # Removes element at index 3
print(numbers)


numbers[1] = 227           # Updates the value at index 1 by 227. Because, Lists are mutable (changeable)
print(numbers)

tuple = (1, 2, 3)
print(type(tuple))         # Tuples are immutable
print(tuple)

# Swapping of two numbers
a = 1
b = 2
a, b = b, a
print(a, b) 
