''' Topic hai
str()
int()
float()

'''

var1 = "Hello World !!" # String Variable jo double quote ke andar hai wo hamesa string hi rhta hai
var2 = "4"              # Integer Variable
var3 = 38.2             # Float Variable
var4 = "Singhal"        # String Variable
var5 = "10"             # Integer Variable


print(var1)           #ye print kr dega hello world ko 
print(type(var1))     #ye print hello world ko nhi karega balki uska type batayega means string
print(var1 + var2)    #ye to bs dono ko direct print kr dega ( hello world 4)
print(var1 + var4)    #same kahani 
#print(var2 + var3) #Run nhi hoha kyuki hm ek string aur ek float ko add krna cha rhe hai. agla line run karega.
print(int(var2) + var3)

# print(var2+var5) 
# now it is concatenating matlab error show kr dega bhai kyu kyuki maschine usko int ke form me nhi le rha. to usko int banao bhai.
# now  agla line kro run karega try kro 

print(int(var2) + int(var5)) # Type casting example. Ye run karega.




print(10 * "Hello World !!!\n")             # Iske through hello world 10 times print hoga
print(100 * (int(var5) + int(var2)))        # int(var5) + int(var2) iska value 14 aega ab usko bhi ham multiply kr sakte hai. ans is 1400
print(100 * str(int(var5) + int(var2)))     # add hone baad wo 14 bana jisko ham str() iska matlab ab maschine 14 ko 100 times likh dega