"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# found: x = datetime.datetime(2020, 5, 17) --> sets a date of 05-17-2020 to x
# found: y = datetime.datetime.today() --> sets a date if 09-01-2020 (as of this writing) to y
# found: print(y.month) would return 9
# found: print(x.day) would return 17
# found: print(y.year) would return 2020
# found: print(x.strftime("%B")) would convert 5 to May (full name of month)
# found: print(x.strftime("%b")) would convert 5 to May (short name of month)

def showdate(month, year):
    if(month is '0'):
        mth = datetime.today()
        print("Month:", mth.strftime("%B"))
    else:
        mth = datetime(2020, int(month), 1)
        print("Month:", mth.strftime("%B"))

    if(year is '0'):
        print("Year:", datetime.today().year)
    else:
        print("Year:", year)

if __name__ == "__main__":
    # print("Total Arguments:", len(sys.argv))
    # argument 0 should be the file name called
    # argument 1 should be the month
    # argument 2 should be the year
    if(len(sys.argv) >= 3):
        showdate(sys.argv[1], sys.argv[2])
    elif(len(sys.argv) == 2):
        showdate(sys.argv[1], '0')
    else:
        showdate('0', '0')
