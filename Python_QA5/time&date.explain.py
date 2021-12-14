import time

#הזמן בשניות שעבר מ1.1.1970
print(time.time())

#  הזמן הנוכחי עכשיו במדוייק בצורה לא מסודרת
print(time.localtime())

#זמן של השהייה
print(time.sleep(1))

#  הזמן במשווה כדור הארץ בצורה לא מסודרת
print(time.gmtime())

#מדפיס את התאריך והשעה הנוכחי בתצוגה יפה
print(time.asctime())

#מדפיס את התאריך והשעה בתצוגה יפה מאז 1.1.1970
print(time.ctime())

import datetime

#הזמן המדויק של עכשיו
print(datetime.datetime.now())

#(חיסור) כמה זמן יעבור עד התאריך בסוגריים
print(datetime.datetime(2022,1,1,00,1,1)-datetime.datetime.now())

# (זמן כולל) הזמן עכשיו פלוס זמן שמגדירים
print(datetime.datetime.now() + datetime.timedelta(minutes=10))


import datetime
x = datetime.datetime.now() + datetime.timedelta(days=10)
x.date()
print(x.time())

print(datetime.datetime(2019,1,1,00,1,1)!=datetime.datetime(2018,1,1,00,1,1))

now = datetime.datetime.now()

#מחזיר רק את השנה
year = now.strftime("%Y")
print("year:",year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%d/%m/%Y,%H:%M:%S")
print("date and time:",date_time)

import datetime

# חיסור תאריכים
# print(datetime.datetime(2022, 6, 27, 00, 1, 1)-datetime.datetime.now())

# להראות רק תאריך בעוד 12 ימים:
# x = datetime.datetime.now() + datetime.timedelta(days=12)
# print(x.date())
#
# # להראות רק שעה בעוד 12 ימים:
# x = datetime.datetime.now() + datetime.timedelta(days=12)
# print(x.time())

# אם תאריכים שונים אחד מהשני
# print(datetime.datetime(2019, 8, 3) < datetime.datetime(2016,9,7))

