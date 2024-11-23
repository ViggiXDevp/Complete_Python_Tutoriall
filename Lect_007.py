# if-else & Elif use krte hai.

num1 = int(input("Enter your 1st Number : "))
num2 = int(input("Enter your 2nd Number : "))
num3 = int(input("Enter your 3rd Number : "))
if num1>num2:
    print("number 1 is Greater than 2.")
elif num1<num2:
    print("number 1 is lesser than 2.")
elif num1==num2:
    print("Equal")    
elif num1>num3:
    print("number 1 is Greater than 3.")    
elif num1<num3:
    print("number 1 is lesser than 3.")   
elif num1==num3:
    print("number 1 is equal to number 3")     
elif num2>num3:
    print("number 2 is Greater than 3.")    
elif num2<num3:
    print("number 2 is lesser than 3.")   
elif num2==num3:
    print("number 2 is equal to number 3")        
else:
      print("Your input is wrong")



'''A Programm for checking NUmber is in list or not '''

list1 = [5, 7, 3]
print(5 in list1)
if 5 in list1:
  print("Yes, it is in the list.")


''' A programm For Eligibility for driving '''

age1 = int(input("Enter your Age : "))
if age1>18:
    print("Eligible for driving.")
elif age1==18:
    print("Please came back after sometime.")
else:
    print("Not Eligible for driving.")