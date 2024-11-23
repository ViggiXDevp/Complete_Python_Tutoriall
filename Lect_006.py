# set function ka Use !!!  
'''
   1)sets me kaise bhi no. ko likh print me wo sahi kr dega aacendinge order me.
   2) koi bhi duplicate no. pr error show kr dega.
'''

s1 = set([10,8,3,4,5,6,7,9,1,2,"Singhal"])    
s2 = set([10,200,300])
s3 = {5,4,6,7,8}
s4 = {1,2,3,4,5}         # Sets likhne ka dusra trika.
print(s1)                # Mera set1 ko print kr dega.
print(s2)                # Mera set2 ko print kr dega.
print(s3)                # Mera set3 ko print kr dega.     
print(type(s1))          # Mere set1 ka type print karega jo ki set hai.
print(len(s1))           # Mere Set1 me kitna elements hai wo likh dega.

# Elements remove kaise kare.
s1.remove("Singhal")
print(s1)          

# Elements add kaise kare.
s1.add(11)
print(s1)

# Elements ko ek baar me clear kaise kare.
s1.clear()
print(s1)

'''union aur intersection function s3 aur s4 ke liye hi kaam karega 
   s1 aur s2 ke liye nhi karega kyuki wo old version ka typing hai'''

# Elemnts ka Union lete hai.
s5 = s4.union(s3)
print(s4)

# Elements ka intersection lete hai.
s6 = s3.intersection(s4)
print(s6)

s6 = s3 | s4
print(s6)

