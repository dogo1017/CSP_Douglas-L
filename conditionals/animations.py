# main.py

import time
import sys

animation = "13456789_-_-_-_-_-_-|_|"
start_time = time.time()
while True:
    for i in range(24):
        time.sleep(0.9)  # Feel free to experiment with the speed here
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    if time.time() - start_time > 100:  # The animation will last for 10 seconds
        break
sys.stdout.write("\rDone!")

#It waorks