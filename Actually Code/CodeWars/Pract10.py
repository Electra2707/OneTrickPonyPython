"""Your task in order to complete this Kata is to write 
a function which formats a duration, given as a number of 
seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is
zero, it just returns "now". Otherwise, the duration is 
expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like
4 seconds, 1 year, etc. In general, a positive integer 
and one of the valid units of time, separated by a space. 
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space 
(", "). Except the last component, which is separated
by " and ", just like it would be written in English.

A more significant units of time will occur before
than a least significant one. Therefore, 1 second 
and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times.
So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value 
happens to be zero. Hence, 1 minute and 0 seconds
is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible".
It means that the function should not return 61 seconds,
but 1 minute and 1 second instead. Formally, the duration
specified by of a component must not be greater than any 
valid more significant unit of time.

"""
import datetime


def format_duration(seconds: int) -> str:
    seconds = abs(seconds)
    if seconds <= 59:  # Only seconds
        if seconds == 0:
            now = datetime.datetime.today()
            return now.strftime("%H hours, %M minutes and %S seconds")
        elif seconds == 1:
            return f"{seconds} second"
        else:
            return f"{seconds} seconds"
    elif seconds >= 60 and seconds <= 3599:  # With minutes until 59min
        if seconds == 60:
            return "1 minute"

    elif seconds >= 3600 and seconds <= 86399:  # With hours until 23hours
        if seconds == 3600:
            return "1 hour"

    elif seconds >= 86400 and seconds <= 3.145e+7:  # With days until 364days
        if seconds == 86400:
            return "1 day"
    else:  # Work with years
        if seconds == 3.154e+7:
            return "1 year"
        # time_reach_hours = (time_reach_seconds)

        # raw_time = datetime.datetime.fromtimestamp(seconds)
        # return raw_time.strftime("%D days, %H hours, %M minutes, %S seconds")


print(format_duration(0))  # , "1 second")
print(format_duration(1))  # , "1 second")
print(format_duration(62))  # , "1 minute and 2 seconds")
print(format_duration(120))  # , "2 minutes")
print(format_duration(3600))  # , "1 hour")
print(format_duration(3662))  # , "1 hour, 1 minute and 2 seconds")
