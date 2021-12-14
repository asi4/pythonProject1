# כתיבת מספר מהסוף להתחלה
num = int(input("enter 3 digit number: "))

s = (num%10) #singularity
d = (num//10%10) #dozens
h = (num//100%10) #hundreds

print(f"{s}{d}{h}")


# לחבר ספרות למספר ולבצע פעולות במספר
num1 = int(input("enter 1 digit number1: "))
num2 = int(input("enter 1 digit number2: "))
num3 = int(input("enter 1 digit number3: "))

print(f"{num1}{num2}{num3}")
num = (num1*100+num2*10+num3)
print(2*num)



# מציאת חלוקה שלמה בין שני מספרים,
# מציאת חלוקה עשרונית ושארית.
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))

complette = (num1//num2)
esronit = (num1/num2)
sheerit = (num1%num2)

print(f"{complette}, {esronit}, {sheerit}")