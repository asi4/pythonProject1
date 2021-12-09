# לולאה פשוטה תרגיל 3:
# num1 = int(input("enter 1 number: "))
# num2 = int(input("enter 2 number: "))
#
# while  num1%2==0 and num2%2==0:
#         print(num1+num2)
#         num1 = int(input("enter 1 number: "))
#         num2 = int(input("enter 2 number: "))
# print(num1*num2)

# # תרגיל 4: כל עוד סכום המספרים 10, להמשיך לקלוט מספרים
# num1 = int(input("enter 1 number: "))
# num2 = int(input("enter 2 number: "))
#
# while (num1+num2 == 10):
#     num1 = int(input("enter 1 number: "))
#     num2 = int(input("enter 2 number: "))
#
# #  לולאה ומספר עם 3 ספרות# תרגיל 1:
# num = int(input("enter 3 digit number: "))
# while 999>=num>=100:
#     print((num//100)+(num//10%10)+(num%10))
#     num = int(input("enter 3 digit number: "))
# print("error")

# # #תרגיל 2:
# age = int(input("enter you age: "))
# while 0<=age<=120:
#     while 0<=age<=18:
#         print("child")
#         age = int(input("enter you age: "))
#     while 19<=age<=60:
#         print("adult")
#         age = int(input("enter you age: "))
#     while 61<=age<=120:
#         print("senior")
#         age = int(input("enter you age: "))
# print("NOT")

# תרגיל 5:
num = int(input("enter number: "))
while 100>num>9:
    while (num%7==0) and num>=10:
        print("Luck")
        num = int(input("enter number: "))
    while ((num%10==7) or (num//10==7)) and num>=10:
        print("Luck")
        num = int(input("enter number: "))
    num = int(input("enter number: "))
