import datetime

moon_landing = "7/20/1969"
moon_landing_datetime =datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)