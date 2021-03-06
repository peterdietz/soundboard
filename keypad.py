from pad4pi import rpi_gpio
import time
from soundboard import Soundboard
soundboard = Soundboard()
soundboard.play_sound(Soundboard.STARTUP_KEY)


def process_key(key):
    soundboard.play_sound(key)


# Setup Keypad
KEYPAD = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"],
    ["*","0","#"]
]

ROW_PINS = [19, 26, 20, 21] # BCM numbering
COL_PINS = [5, 6, 13] # BCM numbering

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
keypad.registerKeyPressHandler(process_key)

try:
    while 1:
        time.sleep(.5)
except KeyboardInterrupt:
    print("Keyboard interupt")
except:
    print("exception")
finally:
    print("Closing")
    soundboard.play_sound(Soundboard.SHUTDOWN_KEY)
    time.sleep(3)
    keypad.cleanup()
