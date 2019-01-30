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
        pygame.mixer.init(48000, -16, 1, 1024)
        self.soundboard = {
            '0': pygame.mixer.Sound("sounds/buzzer.wav"),
            '1': pygame.mixer.Sound("sounds/clap.wav"),
            '2': pygame.mixer.Sound("sounds/CastleThunder.wav"),
            '3': pygame.mixer.Sound("sounds/whats-happening.mp3")
        }
        print("Soundboard Ready.")

    def play_sound(self, key):
        try:
            print(key)
            if key in self.soundboard:
                self.soundboard[key].play()
            else:
                print("No sound registered at {}".format(key))
        except Exception as e:
            print(e)
            pass



