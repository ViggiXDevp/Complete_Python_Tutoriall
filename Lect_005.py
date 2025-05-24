# ======== Dictionaries ========
# ...Syntax...
'''d1 = {"Key" : "Value"}
print(type(d1))
print(d1) '''

d2 = { "2017": "Maaya",
       "2016": "Naagin",
       "web-series": {"1":"Sacred Games", "2":"Mirzapur", "3":"Deadpool 2"}}   # Nested Dictionary
d2["2018"] = "Simba"      # Adding a key value pair in d2. Here, it is {"2018" : "Simba"}

print(d2["web-series"])   # Printing a dictionary which is a value for key "web-series".
print(d2)                 # Final output of d2 dictionary

del d2 ['2018']           # Use del keyword if you want to delete any pair.
print(d2)                 # Updates the dictionary
#print(d2["2018"])        # If you try to print this it will throw an error because, it is already deleted.


d3 = d2.copy()            # It will create new dictionary by copying from d2 dictionary
del d3["2017"]            # This will delete the '2017' key value pair of d3 dictionary but, not d2.
print(d3)


print(d2.get("2017"))     # Used to get value by giving it's key as input


d2.update({"2019" : "URI"})    # Used to update the dictionary
print(d2)                      # Get your final output

print(d2.keys())
print(d2.items())
