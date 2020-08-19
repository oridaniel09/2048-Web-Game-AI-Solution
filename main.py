from selenium import webdriver
from input import update_location
from movement import move
import time

# Variables
driver = webdriver.Chrome()

# Defining what website to use
driver.get('https://play2048.co/')

board = ([0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0])

tile_container = driver.find_element_by_class_name("tile-container")

# MAIN
# driver.implicitly_wait(1)
move('right', tile_container, board)
time.sleep(0.5)
move('left', tile_container, board)

time.sleep(10)
driver.quit()
