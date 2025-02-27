# Douglas London, time of day python

import time
current = time.time()
local_time = time.localtime(current)
hour = local_time.tm_hour # millitary time (0-23)

if(hour < 12):
    print("Good morning!")
elif(hour < 17):
    print("Good afternoon!")
else:
    print("Good evening!")
