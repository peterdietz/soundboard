import pygame.mixer
import RPi.GPIO as GPIO
from time import sleep
from sys import exit

GPIO.setmode(GPIO.BCM)

pins = [5, 6, 13, 19, 20, 21, 26]
for pin in pins:
    GPIO.setup(pin,GPIO.IN)

pygame.mixer.init(48000,-16,1,1024)

soundA = pygame.mixer.Sound("sounds/buzzer.wav")
soundB = pygame.mixer.Sound("sounds/CastleThunder.wav")
soundC = pygame.mixer.Sound("sounds/Scream.wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)

print("Soundboard Ready.")


def print_pin(number):
    state = GPIO.input(number)
    print("Pin {} == {}".format(number, state))


while True:
    try:
        print_pin(5)
        print_pin(6)
        print_pin(13)
        print_pin(19)
        print_pin(20)
        print_pin(21)
        print_pin(26)

        if(GPIO.input(22) == True):
            soundChannelA.play(soundA)
            print("soundA")
        if(GPIO.input(23) == True):
            soundChannelB.play(soundB)
            print("soundB")
        if(GPIO.input(24) == True):
            soundChannelC.play(soundC)
            print("soundC")
        sleep(.01)

    except KeyboardInterrupt:
        exit()
