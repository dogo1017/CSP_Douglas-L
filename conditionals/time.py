# Douglas London, Time python
import time

#first instance of time in programming
first_time = time.gmtime()
#print(first_time)

#current time in seconds
current = time.time()
#print(curent) #seconds since 1970

#Current date and time like we see it

now = time.ctime(current)
#print(now)

#getting part of time

local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour # millitary time (0-23)
print(hour)