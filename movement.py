from pynput.keyboard import Key, Controller
import time
from input import update_location

keyboard = Controller()


def move(direction, tile_container, board):
    if direction == 'up':
        key = Key.up
    if direction == 'down':
        key = Key.down
    if direction == 'left':
        key = Key.left
    if direction == 'right':
        key = Key.right
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)
    update_location(tile_container, board)
