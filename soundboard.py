import pygame.mixer


class Soundboard:
    """
    Ensure there is a sound for each numbered slot
    0 => sounds/buzzer.wav,
    ...

    Use me like this:
    soundboard = Soundboard()
    soundboard.playSound(0)
    """
    def __init__(self):
        self.mixer = pygame.mixer.init(48000, -16, 1, 1024)
        sndA = pygame.mixer.Sound("sounds/buzzer.wav")
        sndB = pygame.mixer.Sound("sounds/clap.wav")
        sndC = pygame.mixer.Sound("sounds/CastleThunder.wav")
        self.soundboard = {0: sndA, 1: sndB, 2: sndC}
        print("Soundboard Ready.")

    def play_sound(self, number):
        print(number)
        if number in self.soundboard:
            self.soundboard[number].play()
        else:
            print("No sound registered at {}".format(number))



