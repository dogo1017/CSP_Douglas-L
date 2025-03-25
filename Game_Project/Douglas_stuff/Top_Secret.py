import pygame
import time

# Initialize pygame mixer for audio functionality
pygame.mixer.init()


try:
    # Load a sound file (replace 'your_sound_file.wav' with the path to your audio file)
    sound = pygame.mixer.Sound('batman_theme_x.wav')

    # Play the sound
    sound.play()

    # Wait for the sound to finish playing
    time.sleep(sound.get_length())

    print("Sound has finished playing.")
except:
    print("there was an error")
    # ask for inpuyt
    # if no, die
    

print("this will always run")