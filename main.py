from soundboard import Soundboard
from time import sleep
from sys import exit


soundboard = Soundboard()
while True:
    try:
        soundboard.play_sound(0)
        sleep(1)
        soundboard.play_sound(1)
        sleep(1)
        soundboard.play_sound(2)
        sleep(1)
        soundboard.play_sound(19)
        # TODO: Wire up keypad and/or keyboard
        sleep(1)
    except KeyboardInterrupt:
        exit()

