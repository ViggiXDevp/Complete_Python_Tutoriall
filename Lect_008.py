# For loops in Python.

list1 = ["Rahul", "Dheeraj", "Avinash", "Tia"]
for item in list1:
  print(item)
list2 = [ ["Rahul", 1], ["Dheeraj", 2], ["Avinash", 3], ["Tia", 4] ]
for item in list2:
  print(item)

dict1 = dict(list2)                  # Lists Se Dictionary Kaise Banaye
print(dict1)

#for item, rank in dict1.items():     # Item ka istemaal.
#     print(item,"rank is", rank)

#for item in dict1:                    # Jo Naya Dictionary Bana hai uska Item ko Print Kr dega.
#     print(item)

items = [int, float, "Rahul", 26, 45, 54, 78, 74, 3, 5]
for item in items:                           # Items me jo special hai usko print Kr wa diye.
    if str(item).isnumeric() and item >= 3:
        print(item)