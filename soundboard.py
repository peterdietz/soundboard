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
        pygame.init()
        pygame.mixer.init(48000, -16, 1, 1024)
        self.soundboard = {
            '0': "sounds/buzzer.wav",
            '1': "sounds/clap.wav",
            '2': "sounds/CastleThunder.wav",
            '3': "sounds/whats-happening.mp3"
        }
        print("Soundboard Ready.")

    def play_sound(self, key):
        try:
            print(key)
            if key in self.soundboard:
                file_name = self.soundboard[key]
                pygame.mixer.music.load(file_name)
                pygame.mixer.music.play()
            else:
                print("No sound registered at {}".format(key))
        except Exception as e:
            print(e)
            pass



