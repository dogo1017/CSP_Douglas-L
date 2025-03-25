import pygame
import time

# Initialize pygame mixer for audio functionality
pygame.mixer.init()

# Load a sound file (replace 'your_sound_file.wav' with the path to your audio file)
sound = pygame.mixer.Sound('your_sound_file.wav')

# Play the sound
sound.play()

# Wait for the sound to finish playing
time.sleep(sound.get_length())

print("Sound has finished playing.")
