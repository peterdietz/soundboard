from pad4pi import rpi_gpio
import time

def processKey(key):
    print(key)

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

keypad.registerKeyPressHandler(processKey)
while 1:
    time.sleep(1)
keypad.cleanup()
