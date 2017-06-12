year = int(input())
month = int(input())

def loop(year):
    if ((not year % 4) and (year % 100)) or not(year % 400):
        return True
    else:
        return False
    
def month_day(year, month):
    if month in(1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in(4, 6, 9, 11):
        return 30
    elif loop(year):
        return 29
    else:
        return 28

def days(year, month):
    day = 0
    if year == 1800:
        for i in range(1, month + 1):
            day += month_day(year, i)
    else:
        for i in range(1800,year):
            if loop(i):
                day += 366
            else:
                day += 365
        for j in range(1, month + 1):
            day += month_day(i + 1, j)
    return day - 1

print (days(year, month) % 7 + 3) % 7
