# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.


monthsWith30d = [4, 6, 9, 11]


def isLeapYear(year):
    # https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
    # If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
    # If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
    # If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
    # The year is a leap year (it has 366 days).
    # The year is not a leap year (it has 365 days).

    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 28:
        return year, month, day + 1
    if day < 30 and month != 2:
        return year, month, day + 1

    if month == 2 and isLeapYear(year) and day <= 28:
        return year, month, day + 1
    elif day == 29 and month == 2:
        return year, month + 1, 1

    if day == 30:
        if month in monthsWith30d:
            return year, month + 1, 1
        else:
            return year, month, day + 1

    if month == 12:
        return year + 1, 1, 1
    else:
        return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        print(result, answer)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()
