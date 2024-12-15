import sys
time = sys.argv[1]
year, Day = time.split('_')
year = int(year)
Day = int(Day)

def isLeapYear(year):
    condiction1 = year % 4
    condiction2 = year % 100
    condiction3 = year % 400
    if (condiction1 == 0 and condiction2 !=0):
        return True
    elif condiction3 == 0 :
        return True
    else:
        return False

def modDate(year, month, day):
    if (day <= 0 ):
        month -= 1
        if month == 2 :
            if (isLeapYear(year)):
                day = 29 + day
            else:
                day = 28 + day
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            day = 31 + day
        else :
            day = 30 + day
    if (month == 2 and day == 29 and not isLeapYear(year)):
        month +=1
        day = 1
    return month, day

def calcDate(year, Day):
    month = Day // 30 + 1
    day = Day
    if (month == 2 ):
        day = Day - 31
    elif(month > 2 and month < 9):
        day = Day - 30 * (month - 1 ) - int(month /2 ) + 1
    elif(month >= 9):
        day = Day - 30 * (month - 1) - int((month - 1)/2 )
    if (month > 2 and not isLeapYear(year) ):
        day += 1
    month, day = modDate(year, month, day)
    return month, day

if Day > 366 and isLeapYear(year):
    print(f'{year:04d} year no so many ({Day}) days')
    exit(0);
elif Day > 365 and not isLeapYear(year):
    print(f'{year:04d} year no so many ({Day}) days')
    exit(0);
month, day = calcDate(year, Day)
print(f'{year:04d}-{month:02d}-{day:02d}')