'''
9. Take two datetimes from user start_time and end_time. Calculates the difference between start_time and end_time by removing night intervals (12 AM to 6 AM). (Hint: You can use python intervals module)
'''

import datetime
# start_time = input("enter time in this format yyyy-mm-dd time:- ")
# time=datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
# print(time)
# end_time = input("enter time in this format yyyy-mm-dd time:- ")
# time=datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
# print(time)
start_time=datetime.datetime(2022,12,25,12,00,00)
print(start_time)

end_time=datetime.datetime(2022,12,30,12,00,00)
print(start_time)

dif = end_time - start_time
print(type(dif))
night_time = datetime.timedelta(hours=30)
new_time= dif - night_time
print(new_time)