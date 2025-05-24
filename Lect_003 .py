# === STRINGS (Slicing & Other functions) ===

mystr = "python is very vast language."                          

'''1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29        What we read as

   p y t h o n   i s     v  e  r  y     v  a  s  t     l  a  n  g  u  a  g  e  .

   0 1 2 3 4 5 6 7 8 9   10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28  <= INDICES...   What compiler reads   '''

"Now, we will understand about some functions..."

print(len(mystr)) # The len function is used to print the length of the string.

print(mystr[0:6]) # This is Slicing...It will print "python" i.e; From index 0 to 5...[Note: Index 6 won't be included].

print(mystr.count("vast"))  # The count function is used to print the number of times a sub-string appears in the main string.

print(mystr[0:6:2]) # This is Slicing with step value...It will print "pto"...starting from index 0 goes till index 5 by printing every second letter.

print(mystr[::3]) # Starts from index 0 and goes till the end i.e; len(mystr) by printing every third letter. 

print(mystr[::-3]) # Starts from the last index and goes upto index 0 by printing every third letter

print(mystr.endswith("uage.")) # The endswith with function checks if the main string ends with the sub-string.

print(mystr.startswith("pyth")) # The startswith with function checks if the main string starts with the sub-string.

print(mystr.capitalize()) # The capitalize function is used to convert the FIRST letter of string to uppercase.

print(mystr.find("very")) # The find function gives the index of the starting letter of the sub-string, when it first time occurs in the main string.

print(mystr.lower()) # The lower function converts entire string to lowercase.

print(mystr.upper()) # The upper function converts entire string to uppercase.

print(mystr.replace("very", "a")) # The replace function .replace("old word", "new word") replaces old word to a new word.
