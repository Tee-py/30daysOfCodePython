
def magic_dates(date):
    """A python function that returns a Bool if a date is magic date or not"""
    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
    months_days = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31,
              'september': 30, 'october': 31, 'november': 30, 'december': 31}
    month = date.split(' ')[0]; day = date.split(' ')[1].split(',')[0]; year = date.split(' ')[1].split(',')[1]
    if month.lower() not in months.keys(): return 'Invalid month'
    elif month.lower() == 'february' and int(day) > 29: return 'February has 28 days in a year or 29 in a leap year'
    elif int(day) <= 0 or months_days[month.lower()] < int(day):
        if month.lower() != 'february': return 'Invalid day. day should be a positive integer and must be in the month'
        else:
            if int(day) > 29: return 'February has 28 days in a year or 29 in a leap year'
            elif int(day) <= 0: return 'Invalid day. day should be a positive integer and must be in the month'
            else: return False
    else:
        if months[month.lower()]*int(day) == int(year[2:]): return True
        else: return False

print(magic_dates('June 9,1990'))
def count_magic(year):
    """A python function that returns a list of all magic dates in a year"""
    if type(year) != int:
        return 'Invalid argument passed; year should be an integer'
    months = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31,
              'september': 30, 'october': 31, 'november': 30, 'december': 31}
    month_list = list(months.keys())
    all_magic_dates = []
    for month in month_list:
        for i in range(1, months[month]+1):
            date = str(month)+' '+str(i)+','+str(year)
            if magic_dates(date)==True:
                all_magic_dates.append(date)
    return all_magic_dates

print([count_magic(i) for i in range(2000,3000)])