import pygame.mixer
import RPi.GPIO as GPIO
from time import sleep
from sys import exit

GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.IN)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)

pygame.mixer.init(48000,-16,1,1024)

soundA = pygame.mixer.Sound("sounds/buzzer.wav")
soundB = pygame.mixer.Sound("sounds/CastleThunder.wav")
soundC = pygame.mixer.Sound("sounds/Scream.wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)

print("Soundboard Ready.")

while True:
    try:
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
