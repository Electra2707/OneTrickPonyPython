"""_summary_

"""


def is_leap(year: int):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 !=0):
        return True
    return False

print(is_leap(1992))
