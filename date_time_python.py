import datetime

currDate = datetime.datetime.now()
print("Current year is: " + str(currDate.year))
print("Current day of the month is: " + str(currDate.strftime("%d")))
print("Current day of the week is: " + str(currDate.strftime("%A")))
print("Current month of the year is: " + str(currDate.strftime("%B")))
print("Current date in local version is: " + str(currDate.strftime("%x")))


