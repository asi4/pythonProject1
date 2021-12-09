# מציאת חלוקה שלמה בין שני מספרים,
# מציאת חלוקה עשרונית ושארית.
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))

complette = (num1//num2)
esronit = (num1/num2)
sheerit = (num1%num2)

print(f"{complette}, {esronit}, {sheerit}")
