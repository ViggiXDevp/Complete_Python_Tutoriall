# ========= Sets =========
'''
   *** Points to Ponder ***
   1) When you print a set, it will arrange itself in an ascending order.
   2) Only unique values will be printed in the set even if there are duplicates in the input.
'''

s1 = set([10,8,3,4,5,6,7,9,1,2,"Vighnesh"])    
s2 = set([10,200,300])
s3 = {5,4,6,7,8}
s4 = {1,2,3,4,5}         # Another way to represent sets
print(s1)                # Prints set s1
print(s2)                # Prints set s2
print(s3)                # Prints set s3     
print(type(s1))          # Prints type of set s1
print(len(s1))           # Prints length of set s1

# Removing elements from a given set
s1.remove("Vighnesh")
print(s1)          

# Adding elements to a given set
s1.add(11)
print(s1)

# Deleting the entire set
s1.clear()
print(s1)

# Taking Union of two sets
s5 = s4.union(s3)
print(s5)

s5 = s3 | s4  # Another way for Union
print(s5)

# Taking Intersection of two sets
s6 = s3.intersection(s4)
print(s6)

s6 = s3 & s4  # Another way for Intersection
print(s6)


