import datetime
#
mybirthday = datetime.datetime(1961,5,31,12,0,0)
print("My birthday:", mybirthday)
rightnow = datetime.datetime.now()
print("Right now:",rightnow)
#   create a timedelta
timedelta1 = rightnow - mybirthday
print(" ")
print(timedelta1)
# print(timedelta1.days)
# print(timedelta1.seconds/3600)


