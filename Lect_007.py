# ======== if, elif and else statements ========

num1 = int(input("Enter your 1st Number : "))
num2 = int(input("Enter your 2nd Number : "))
num3 = int(input("Enter your 3rd Number : "))
if (num1 > num2 and num1 > num3):
    print("num1 is greater")
elif(num2 > num1 and num2 > num3):
    print("num2 is greater")
elif(num3 > num1 and num3 > num2):
    print("num3 is greater")
else:
      print("Your input is wrong")


''' Checking whether the number is present in the list '''

list1 = [5, 7, 3]
print(5 in list1)
if 5 in list1:
  print("Yes, it is in the list.")


''' Checking the eligibility criteria for driving license '''

age = int(input("Enter your age : "))
if age >= 18:
    print("Eligible for permanent driving license.")
elif age >= 16:
    print("Eligible for learner's license (for non-geared vehicles).")
else:
    print("Not eligible for any driving license.")
