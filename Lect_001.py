# === Comments, Escape Sequence and Print Statements ===

# This is first comment example.
print("Hello Guyzz!!!")  # print statement is used to print the content present in between " ". Anything which is present in between " " is a string.

'''
Multi line comment example. 
With triple qoute we can comment multiple lines.
'''

# By using end="", it overrides the \n function. So the second line will get printed in the first itself.
print("This is first line.", end="")
print("This is second line.")

# Here also, second line gets printed in the first but with a space between both lines because, end=" " considered as space between those lines
print("This is first line.", end=" ")
print("This is second line.")

# Here, first line ends with a comma
print("This is first line", end=",")
print("This is second line.")


# Now Singhal ab new line me print hoga.
print("Hello I will print my name in the next line using escape sequence \nVighnesh Reddy")
print("Thank you...")
