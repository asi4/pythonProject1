# למצוא את השנה שאדם יהיה בן 100
name = input("enter your name: ")
age = int(input("enter your age: "))

a = 100-age
import datetime

x = datetime.datetime.now() + datetime.timedelta(a*365)
x.date()
now = x
year = int(now.strftime("%Y"))

print(f"in year {year}, {name} will be 100 years old.")

# פורמט אירופאי יום-חודש-שנה
import datetime
now = datetime.datetime.now()
now.date()

year = int(now.strftime("%Y"))
month = now.strftime("%m")
day = now.strftime("%d")
print(f"{day}/{month}/{year//1000}{year%10}")

#פורמט אמריקקי
print(f"{month}/{day}/{year//1000}{year%10}")


