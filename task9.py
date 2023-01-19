'''
9. Take two datetimes from user start_time and end_time. Calculates the difference between start_time and end_time by removing night intervals (12 AM to 6 AM). (Hint: You can use python intervals module)
'''
from datetime import datetime,timedelta,date,time
import portion  as P
#input date & time
start_time = input('Please enter a start date :- ')
end_time = input('Please enter a end date :- ')

#convert string to datetime object
start_time = datetime.strptime(start_time,'%Y-%m-%d %H:%M:%S')
end_time = datetime.strptime(end_time,'%Y-%m-%d %H:%M:%S')

#difrent between    
dif_start_and_end= end_time - start_time

#time convert to startime 
my_date = start_time.date()
my_time =datetime.min.time()
start_date = datetime.combine(my_date, my_time)

#interval in night time betwen start time to end time
night_interval =[]
while start_date <= end_time:
    i =P.closed(datetime.combine(start_date,time()),datetime.combine(start_date,time())+timedelta(hours=6))
    night_interval.append(i)
    start_date += timedelta(days=1)

#intreval start time to end time
dif_start_to_end_intreval=P.closed(start_time,end_time)
new_night_interval = []
for night_time  in night_interval:
    new_night_interval.append(dif_start_to_end_intreval.intersection(night_time))

#fetch night starttime and endtime
total_night_time =timedelta()
for i in  range(len(new_night_interval)):
    total_night_time = total_night_time + new_night_interval[i].upper - new_night_interval[i].lower

print("It's  time for removing after night time :- ",dif_start_and_end - total_night_time)

