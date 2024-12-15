import sys

def isLeapYear(year):
    condiction1 = year % 4
    condiction2 = year % 100
    condiction3 = year % 400
    if (condiction1 == 0 and condiction2 !=0):
        return True
    elif( condiction3 == 0 ):
        return True
    else:
        return False

def calcDay(year, month, day):
    Day = (month-1) * 30 + day
    if (month == 2 ):
        Day += 1
    elif(month > 2 and month < 9):
        Day += int(month /2 ) -1
    elif(month >= 9):
        Day += int((month - 1)/2 )
    if (month > 2 ):
        if (isLeapYear(year)):
            return Day
        else:
            return Day - 1
    return Day

if __name__ == '__main__':
    time = sys.argv[1]
    year, month, day = time.split('_')
    year = int(year)
    month = int(month)
    day = int(day)
    string2 = str(f'{calcDay(year, month, day):03d}')
    print(str(year) + string2)
