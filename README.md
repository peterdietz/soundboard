# le Soundboard

le Soundboard plays funny music in response to button presses. The perfect setup is a  Raspberry Pi with a 3x4 phone pad plugged into the GPIO pins, and a speaker in the 3.5mm port.

![img_20190130_131357](https://user-images.githubusercontent.com/58014/52070180-3ea22000-254e-11e9-9044-e64e47c17cd4.jpg)
![screen shot 2019-01-31 at 11 50 51 am](https://user-images.githubusercontent.com/58014/52070289-8163f800-254e-11e9-836e-d50d38feca0d.png)



### Installation

Raspberry Pi 3 B+

Install the dependencies and configure cron to start the server on reboot.

```sh
cd /home/pi
git clone https://github.com/peterdietz/soundboard
cd soundboard
pip3 install pygame
pip3 install pad4pi

#To run in keyboard mode
python3 read_keyboard_input.py

#To run in keypad mode (after you've plugged in all GPIO pins)
python3 keypad.py

#To configure crontab to start on reboot
sudo vim /etc/crontab
##Add the following line  to the crontab
@reboot sudo python3 /home/pi/soundboard/keypad.py
## You will have to have installed the above pip dependencies as that user
```

### Tests
To run the tests

```sh
python soundboard/tests/soundboard_test.py
```

### Hardware used
Bought on Adafruit:
- Raspberry Pi 3B+
- Raspberry Pi Case
- 8GB microSD card with pixel desktop noobs preinstalled
- 3x4 phone style matrix keyboard
- female/female jumper wires
- 5v Micro-Usb power supply
- USB powered speakers
