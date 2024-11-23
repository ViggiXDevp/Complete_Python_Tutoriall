# So ab padhenge String Slicing And Other Functions. to first ek string lenge.

mystr = "python is very vast language."                          

'''1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29        Ye Hmlog padhega

   p y t h o n   i s     v  e  r  y     v  a  s  t     l  a  n  g  u  a  g  e  .

   0 1 2 3 4 5 6 7 8 9   10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29    ye maschine Padhega   '''

"to ab alag alag function ka using samajhte hai"

print(len(mystr)) # iska use str me kita length hai wo nikalne ke liye hoga.

print(mystr[0:6]) # iska use alphabet me 0-6 tak yani 1-6 alphabets hai usko niaklne ke liye hoga.

print(mystr.count("vast"))  # strig ke jitne words likhoge uska count batayga.

print(mystr[0:6:2]) # skipping karega alphabets me 1-6 me wo 1-3-5 show karega.

print(mystr[::3]) # alphabet print karega suru se end tak bs skipping 3 ka hoga.

print(mystr[::-3]) # alphabet print karega end se suru tak bs skipping 3 ka hoga.

print(mystr.endswith("language.")) # fn. check karega ki word available hai ki nhi hoga to false warna True

print(mystr.capitalize()) # statement ke first word ke first alphabet ko capitak kr dega.

print(mystr.find("very")) # statement ko khojega aur batayga ki kis no. pr present hai.

print(mystr.lower()) # complete sentence ko ye fn. lower alphabet me likh dega.

print(mystr.upper()) # complete sentence ko ye fn. UPPER alphabet me likh dega.

print(mystr.replace("very", "a")) # Replace krne wala fn. hai.