# Lets talk about Dictionaries.
# structure sikh lo bhai!!!
'''d1 = {"SName" :" Singhal puri"}
print(type(d1))
print(d1) '''

d2 = { "2017": "Maaya",
       "2016": "Naagin",
       "web-series": {"1":"Sacred Games", "2":"Mirzapur", "3":"Deadpool 2"}}      # pehle ek dictionary banaye.
d2["2018"] = "Simba"      # dictionary me add krne ke liye use krte hai.  

print(d2["web-series"])   # dictionary ke andar webseries me kya hai print krne ke use krte hai.
print(d2)                 # Now print krte hai to final output milega.

del d2 ['2018']           # Kuch delete krna hai dictionary se tb use kro.
print(d2)                 # Now print krte hai to final output milega.
#print(d2["2018"])         # ye type kroge to error batayega.


d3 = d2.copy()            # ye ek naya dictionary bana dega jo ki d2 se copy hoga.
del d3["2017"]            # ye d3 ka 2017 ka elemnt ko delete hoga.
print(d3)


print(d2.get("2017"))     # Apne dictionary se kuch output chahiye tb use kro.


d2.update({"Amit":"Lazy Person"})    # Dictionary me kuch update  krna hai tb use kro
print(d2)                             # Get your final result.

print(d2.keys())
print(d2.items())