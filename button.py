from signal import pause
from time import sleep
from gpiozero import LED,Button

button = Button(2)

button.wait_for_press()
print("button")