# # This Program by m.mahadi
# import calendar
#
# def calander(year, month):
#     for i in range(1, month + 1):
#         cal = calendar.month(year, i,5)
#         print(cal)
#
# year, month = map(int, input('Year , month: ').split())
# calander(year, month)

import calendar

year = int(input('Enter a year:'))
month = int(input('Enter a month: '))
cal = calendar.month(year, month, 5)
print(cal)
