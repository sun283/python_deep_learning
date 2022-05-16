# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date

def num_sundays_on_first_of_month(year1, year2):
  num_sundays = 0
  for i in range(year1, year2+1):
      for j in range(1, 13):
          if date(i, j, 1).weekday() == 6:
              num_sundays += 1
  return num_sundays

if __name__ == '__main__':
    print(num_sundays_on_first_of_month(1901,2000))
    
"""How many Sundays fell on the first of the month 
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

counter = 0
year = 1901
month = 1

curr_day = date(year,month,1)

while(curr_day.year < 2001):
	if(curr_day.weekday() == 6):
		counter += 1
	if(month+1 == 13):
		month = 1
		year += 1
	else:
		month += 1
	curr_day = date(year,month,1)

print("Counter: " + str(counter))