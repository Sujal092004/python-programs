from pynput.keyboard import key, Controller

from time import sleep

keyboard = Controller()


def volumeup():
    for i in range(5):
        keyboard.press(key.media_volume_up)
        keyboard.release(key.media_volume_up)
        sleep(0.1)


def volumedown():
    for i in range(5):
        keyboard.press(key.media_volume_down)
        keyboard.release(key.media_volume_down)
        sleep(0.1)
