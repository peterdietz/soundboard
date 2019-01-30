import pygame.mixer


class Soundboard:
    STOP_KEY = "*"
    REPEAT_KEY = "#"
    """
    Ensure there is a sound for each numbered slot
    0 => sounds/buzzer.wav,
    ...

    Use me like this:
    soundboard = Soundboard()
    soundboard.playSound(0)
    """
    def __init__(self):
        pygame.init()
        pygame.mixer.init(48000, -16, 1, 1024)
        self.soundboard = {
            '1': "sounds/boo.mp3",
            '2': "sounds/circus-music.mp3",
            '3': "sounds/whats-happening.mp3",
            '4': "sounds/onshift-mobile-whistle.mp3",
            '5': "sounds/everything-is-awesome.mp3",
            '6': "sounds/bye-bye-lil-sebastian.mp3",
            '7': "sounds/baby-shark.mp3",
            '8': "sounds/farts.mp3",
            '9': "sounds/rick-roll.mp3",
            #'*': STOP
            '0': "sounds/mike-jones.mp3",
            #'#': REPEAT
        }
        print("Soundboard Ready.")

    def play_sound(self, key):
        try:
            print(key)
            if key in self.soundboard:
                file_name = self.soundboard[key]
                pygame.mixer.music.load(file_name)
                pygame.mixer.music.play()
            elif key == Soundboard.STOP_KEY:
                pygame.mixer.music.stop()
            elif key == Soundboard.REPEAT_KEY:
                pygame.mixer.music.play()
            else:
                print("No sound registered at {}".format(key))
        except Exception as e:
            print(e)
            pass



