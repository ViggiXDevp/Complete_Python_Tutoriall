'''
Data Types:
  -> str()
  -> int()
  -> float()
  -> bool()
'''

var1 = "Hiiee Guyzz !!" # String Variable 
var2 = 7                # Integer Variable
var3 = 3.14             # Float Variable
var4 = "Vighnesh"       # String Variable
var5 = 10               # Integer Variable


print(var1)           # This will print Hiiee Guyzz !!
print(type(var1))     # This will print TYPE of the variable, i.e; string
print(var1 + str(var2))    # This will print Hiiee Guyzz !!7. Here, var2 is integer variable. To add to a string variable you should TYPECASTE.

# ***TYPECASTING*** : Type Casting is converting the type of variable from one data type to other to perform concatenation.

print(var1 + var4)    # This wil print Hiiee Guyzz !!Vighnesh 
print(var2 + var3)    # This will print 10.14
print(var4 + str(var5)) # Another type casting example


print(10 * "Hello World !!!\n")             # It will print Hello World !!! for 10 times
print(100 * (int(var5) + int(var2)))        # int(var5) + int(var2) = 70. Now, we will multiply that value with 100
print(100 * str(int(var5) + int(var2)))     # int(var5) + int(var2) = 70 is converted to a string. Now the string "70" will get printed for 100 times
