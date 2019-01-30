from sys import exit
import threading
import queue
import time
from soundboard import Soundboard


def read_keyboard_input(inputQueue):
    print('Ready for keyboard input:')
    while (True):
        # Receive keyboard input from user.
        input_string = input()
        inputQueue.put(input_string)


def main():
    # Background, thread that reads keyboard input and adds to a queue.
    # Foreground, process queue and play sound on soundboard for that input
    input_queue = queue.Queue()
    input_thread = threading.Thread(target=read_keyboard_input, args=(input_queue,), daemon=True)
    input_thread.start()
    soundboard = Soundboard()
    soundboard.play_sound(Soundboard.STARTUP_KEY)

    while True:
        try:
            # Read keyboard inputs
            if input_queue.qsize() > 0:
                input_string = input_queue.get()
                print("input_str = {}".format(input_string))
                soundboard.play_sound(input_string)

                if input_string == "exit":
                    print("Exiting")
                    break

            # Sleep for a short time to prevent this thread from sucking up all of your CPU resources on your PC.
            time.sleep(0.01)
        except KeyboardInterrupt:
            print("Good Bye")
            soundboard.play_sound(Soundboard.SHUTDOWN_KEY)
            exit()

    print("End.")


# If you run this Python file directly (ex: via `python3 this_filename.py`), do the following:
if __name__ == '__main__':
    main()
