#You are given the following information, but you may prefer to do some research for yourself.

#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def sundayCount(start_year, end_year):
    weekday = 0
    first_sunday_count = 0
    for year in range(start_year,end_year):
        if year == 1901:
            first_sunday_count = 0
            
        for month in range(1, 13):
            weekday += 1
            weekday %= 7
            if weekday == 0: first_sunday_count += 1
            if month in [4,6,9,11]: weekday += 30 % 7
            elif month == 2:
                weekday += 28 % 7
                if year % 4 == 0:
                    weekday += 1
                    if year == 1900:
                        weekday -= 1
            else: weekday += 31 % 7
    
    
    return first_sunday_count

if __name__ == '__main__':
    start_year = 1900
    end_year = 2001
    print(sundayCount(start_year, end_year))
