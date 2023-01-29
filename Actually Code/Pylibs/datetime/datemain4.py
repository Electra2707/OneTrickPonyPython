import datetime

now=datetime.datetime.today()
print(now.hour,now.minute,now.second)

print("The current time is",now.strftime("%H:%M:%S"))