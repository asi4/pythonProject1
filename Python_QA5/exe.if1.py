#תרגיל 7: לקלוט יום, חודש ושנה ולבדוק אם תקין
day = input("enter day: ")
month = input("enter month: ")
year = input("enter year: ")

if day == "": day = 1
if month == "": month = 1
if year == "": year = 1950

day=int(day)
if 1<=day<=31: day=int(day)
else: day = 1

month = int(month)
if 1<=month<=12: month=month
else: month = 1

year = int(year)
if 1950<=year<=2020: year = int(year)
else: year = 1950

print(f"{day}/{month}/{year//100%10}{year%10}")

