# Lists aur Lists ke Function ko Samjhte hai.

laptop = ["ram", "battery", "hdd", "led", "wifi", "mouse", 227]

print(laptop[5]) # lists ke 5 yani 6 positiosn wala str. print karega.

numbers = [2, 8, 9, 11, 67, 7]

print(numbers[4]) # lists ke 4 yani 5 positiosn wala int. print karega.
print(numbers[1:4]) # print karega lists ke andar wale integer ko jo 1 se 4 tk ho yani 1 wale 2 wale aur 3 wale tak bs.

# lists ka Max and Min kaise nikale.
print(max(numbers)) # lists ke maximum value wale ke no. ko print karega.
print(min(numbers)) # lists ke minimum value wale ke no. ko print karega.


# lists ka Alat palat ka kaam kaise kare me.
numbers.sort() # sort() fn. ka use lists ke no. ko accending order me daalne ke liye.
print(numbers)
numbers.reverse()  # reverse() fn same hai sort() ka bs list ko palat deta hai.
print(numbers)


#Numbers ko add kaise kare lists me.
numbers.append('10')           #append() ka use kiye kisi bhi no. ya string ko add krne ke liye.
numbers.append('singhal')
numbers.append('1987')
print(numbers)


#lists me index ke hisab se no. ko replace kaise kare.
numbers.insert(1, 54) # list.insert(index no. , change kya krna hai) use hota hai index by replace property ke liye.
numbers.insert(2, 74)
numbers.insert(3, 78)
print(numbers)


#lists me no. ko delete kaise kare.
numbers.pop(1)    #matlab index 1 wala No. delete hoga lists me se.
print(numbers)


#Tuples ka use kaise hota hai!!!
numbers[1] = 227 #tuples basically replacement ka kaam krta hai bs number[index No.] = any No. and yupp you got your new lists.
print(numbers)

Singhal = (1, 2, 3)
print(type(Singhal))
print(Singhal)

# Number Swwapping kaise krte hai.
a = 1
b = 2
a, b = b, a
print(a, b) 