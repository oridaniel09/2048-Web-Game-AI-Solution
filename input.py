from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import re

# finding game box

regex = re.compile(r'-(\d)\b')


def update_location(tile_container, board):
    # parse tile-container html
    html = tile_container.get_attribute('innerHTML')

    # convert to soup
    soup = bs(html, 'lxml')
    divs = soup.find_all('div', attrs={'class': 'tile'})
    for div in divs:
        y, x = regex.findall(div['class'][2])
        x = int(x) - 1
        y = int(y) - 1
        val = regex.findall(div['class'][1])[0]
        board[x][y] = val

    for row in board:
        print(*row)
    print('--------')



