#Douglas London, top scret stuff (; dont PEEK

import os
import sys
import urllib.request

# Function to check and install playsound if missing
def install_playsound():
    try:
        from playsound import playsound
        return playsound
    except ImportError:
        print("Installing required module...")
        os.system(f"{sys.executable} -m pip install playsound")
        from playsound import playsound
        return playsound

# Function to download an MP3 file if it doesn't exist
def download_audio(file_name, url):
    if not os.path.exists(file_name):
        print(f"Downloading default audio file: {file_name}...")
        urllib.request.urlretrieve(url, file_name)
        print("Download complete!")

# Define audio file path
audio_file = "audiofile.mp3"
audio_url = "https://www.soundjay.com/button/beep-07.mp3" # A free beep sound

# Ensure an MP3 file is available
download_audio(audio_file, audio_url)

# Import playsound (after ensuring it's installed)
playsound = install_playsound()

# Play the audio
print("Playing sound...")
playsound(audio_file)
