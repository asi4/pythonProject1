#תרגיל 1
num1 = int(input("enter 1 number: "))
num2 = int(input("enter 2 number: "))
num3 = int(input("enter 3 number: "))
sum = num1+num3+num2
print(sum,(sum/3))

# #תרגיל 2
num1 = int(input("enter 1 number: "))
num2 = int(input("enter 2 number: "))
if num1>num2:
    print(num1+num2)
else: print(num1*num2)

#תרגיל 3
num1 = int(input("enter 1 number: "))
num2 = int(input("enter 2 number: "))
if num1>num2:
    print(num1)
if num2>num1:
    print(num2)
if num1 == num2:
        print("=")

#תרגיל 4
num1 = int(input("enter 1 number: "))
num2 = int(input("enter 2 number: "))
num3 = int(input("enter 3 number: "))
num4 = int(input("enter 4 number: "))
if num1>num2 and num1>num4 and num1>num3:
    print(num1)
if num2 > num1 and num2 > num4 and num2 > num3:
    print(num2)
if num3>num2 and num3>num4 and num3>num1:
    print(num3)
if num4>num2 and num4>num1 and num4>num3:
    print(num4)

#תרגיל 5
movimin = int(input("enter movie length in minutes: "))
h = movimin//60
m = movimin%60
print(f"movie is {h} houres and {m} minutes.")

#תרגיל 6
num1 = int(input("enter 1 number 4 digits: "))
rd = num1%10
print(rd)
#
# #תרגיל 7
num1 = int(input("enter 1 number 4 digits: "))
srd = num1//10%10
print(srd)

#תרגיל 8
num1 = int(input("enter 1 number 2 digits: "))
rd = num1%10
srd = num1//10%10
print(rd+srd)

# תרגיל 9
num1 = int(input("enter 1 int number: "))
if num1%2==0:
    print(num1+2)
else: print(num1+1)

#תרגיל 10
num1 = int(input("enter 1 number: "))
if num1%2==0:
    print("dubble")
else: print("no")

#תרגיל 10
pay = int(input("enter your payment: "))
precent = int(input("enter precent rise: "))
newp = pay+(pay*precent*0.01)
print(newp)
if newp>10000:
    print(newp+(newp*0.05))
