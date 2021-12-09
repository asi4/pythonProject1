# כתיבת מספר מהסוף להתחלה
num = int(input("enter 3 digit number: "))

s = (num%10) #singularity
d = (num//10%10) #dozens
h = (num//100%10) #hundreds

print(f"{s}{d}{h}")
