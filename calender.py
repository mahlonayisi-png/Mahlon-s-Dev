import calendar
import datetime

try:
  year = int(input("Enter year: "))
  month = int(input("Enter month: "))
  cal = calendar.month(year,month)
  print(cal)

  now = datetime.datetime.now()
  print("\n Current Date and Time:")
  print(now.strftime("%y-%m-%d %H:%M:%S"))
except:
    print("Enter numbers only")
