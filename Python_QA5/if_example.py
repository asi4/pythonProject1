# # דוגמא לתנאי בסיסי
#
# num = int(input("enter number: "))
#
# if num>=0:
#     print("positive")
# else: print("negative")

# בודק אם המספר חיובי/שלילי/0
#num = int(input("enter number: "))

#if num>=0:
#    if num == 0:
#        print("zero")
#    else: print("positive")
#if num<0: print("negative")

# בודק אם המספר זוגי או לא זוגי
#num = int(input("enter number: "))
#
#if num%2==0:
#    print("dubble")
#else:print("no dubble")


#תרגיל 3.2: תכנית מקבלת 3 מספרים ומדפיסה את הגדול:
# num1 = int(input("enter number 1: "))
# num2 = int(input("enter number 2: "))
# num3 = int(input("enter number 3: "))
#
# if num1 > num2 and num1 > num3:
#     print(num1)
# if num2 > num1 and num2 > num3:
#     print(num2)
# if num3 > num2 and num3 > num1:
#     print(num3)





# תרגיל 3.3:
num_c = (input("enter number computer you fixed today: "))

if num_c == "":
    num_c = 15
else: num_c = int(num_c)

num_c *= 2
num_c = int(num_c)
print("tommorow fix",num_c)


