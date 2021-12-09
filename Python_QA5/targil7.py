#לקלוט 2 מספרים ולהדפיס אם הסכום שלהם זוגי או לא
#
# num1 = int(input("enter 1 number: "))
# num2 = int(input("enter 2 number: "))
# sum = num1+num2
#
# if sum%2==0:
#     print("dubble")
# else:print("no dubble")

# 2: אם למספר יש 3 ספרות להדפיס את סכום הספרות

# num = int(input("enter 3 digit number: "))
# num1 = num//100
# num2 = num//10%10
# num3 = num%10
# if 100>=num>=999:
#     print(num1+num2+num3)
# else: print("it's not 3 digit number!!!")

#לקלוט גיל להתאים לקבוצה
# age = (input("enter your age: "))
# if age == "":
#     age = 0
# else: age=int(age)
# if 0<=age<=18:
#     print("child")
# if 19<=age<=60:
#         print("adult")
# if 61<=age<=120:
#     print("senior")
#
# age = (input("enter your age: "))
# if age == "":
#     age = 0
# else: age=int(age)
# if 0<=age<=18:
#     print("child")
# elif 19<=age<=60:
#     print("adult")
# elif 60<=age<=120:
#     print("senior")

#תרגיל 4: קלוט 2 מספרים ולהציג את ההפרש בינהם בערך מוחלט
# num1 = int(input("enter 1 number: "))
# num2 = int(input("enter 2 number: "))
#
# num1-=num2
# if num1>=0:
#     print(num1)
# else: print(num1*-1)
#
# #תרגיל 6: בודק אם סכום המספרים הוא 10
# num1 = int(input("enter 1 number: "))
# num2 = int(input("enter 2 number: "))
# if num1+num2==10:
#     print("summary equal 10")
# else: print("summary NOT 10, it's ",num1+num2)


# תרגיל 5: לקלוט שני מספרים ולהדפיס סכום אם הם זוגיים
num1 = int(input("enter 1 number: "))
num2 = int(input("enter 2 number: "))

if num1%2==0 and num2%2==0:
    print(num1+num2)
else: print(num1*num2)
