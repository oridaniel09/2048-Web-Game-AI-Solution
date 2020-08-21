from selenium import webdriver
from movement import move

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
move('left', tile_container, board)