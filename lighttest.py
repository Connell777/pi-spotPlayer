import RPi.GPIO as GPIO

import multiprocessing
import time

# function responsable for doing the heavy work when button1 is pressed
# this function will stop doing the work when button 2 is pressed
def long_processing(e):
    # runs for ever
    while True:
        # waits until the event is set
        e.wait()
        # do work while the event is set
        while e.is_set():
            # do some intensive work here
            print('intensive work...')
            time.sleep(0.5)


if __name__ == '__main__':
    # initialize GPIO buttons
    GPIO.setmode(GPIO.BCM)
    button1_pin = 13
    button2_pin = 12
    GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    first_button_pushed = multiprocessing.Event()

    # GPIO callbacks
    def but1_callback(channel):
        print('first button bushed')
        first_button_pushed.set()

    def but2_callback(channel):
        print('second button bushed')
        first_button_pushed.clear()

    # GPIO callbacks hooks
    GPIO.add_event_detect(button1_pin, GPIO.RISING, callback=but1_callback, bouncetime=300)
    GPIO.add_event_detect(button2_pin, GPIO.RISING, callback=but2_callback, bouncetime=300)

    # a process used to run the "long_processing" function in background
    # the first_button_pushed event is passed along
    process = multiprocessing.Process(name='first_process', target=long_processing, args=(first_button_pushed,))
    process.daemon = True
    process.start()

    while True:
        time.sleep(1)