import pygame  
import time  
  
pygame.init()  # Initialize Pygame  
  
# Initialize the mixer  
pygame.mixer.init()  
  
try:  
    pygame.mixer.music.load('audiomass-output.mp3')    
    pygame.mixer.music.play()    
    time.sleep(0)  
    print("Sound has finished playing.")  
except Exception as e:  
    print("There was an error:", e)  
  
print("this will always run")  

