#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library


DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"
CLIENT_ID="d5bb3dfb8dbe4dec9d658868311f67cf"
CLIENT_SECRET="ff8ea43324b64cf5bc610cbcd2bc2512"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

x=0
def button_callback(channel):
    
                # playing a song
    sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0NrtwAmRAdLxua31SzHvXr'])
    print("song playing")
    sleep(2)
    x=1
#https://open.spotify.com/track/0NrtwAmRAdLxua31SzHvXr?si=87013b70e64245f8
while (True):
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))

    
        # create an infinite while loop that will always be waiting for a new scan
        while (True):            
            print("Waiting for record scan...")
            GPIO.add_event_detect(13,GPIO.FALLING,callback=button_callback)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
        
                
            

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass
    finally:
        if(x==1):
            break