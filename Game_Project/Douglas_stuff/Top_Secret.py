import os  
import pygame  
import time  
import threading  
  
# Function to play music  
def play_music():  
    pygame.init()    
    pygame.mixer.init()  
      
    try:    
        pygame.mixer.music.load('computer-keyboard-typing-290582.mp3')      
        pygame.mixer.music.play(-1)  # Loop the music  
        while pygame.mixer.music.get_busy():  # Wait until the music stops  
            time.sleep(0)  
    except Exception as e:    
        print("There was an error:", e)  
  
# Start music in a separate thread  
music_thread = threading.Thread(target=play_music)  
music_thread.start()  
  
# Your text-typing code here  
input("Type something while the music plays: ")  
print("This will always run.")  
