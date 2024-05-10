'''
John Reiland
NewsTree Kiosk Software
Copyright (c) 2024 John Reiland
'''

# selenium 4
from selenium import webdriver
from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
#https://stackoverflow.com/questions/40002826/wait-for-page-redirect-selenium-webdriver-python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

import pygame   #bring in pygame code
import sys #allows closing of pygame window at end of game

#initialize pygame module
pygame.init()

#init webdriver
options = Options()

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 3.154e+7)

#initialize state list
stateList = ["WELCOME", "NEWS_LIST", "PRINT_COMPLETE"]

#global variable for current state
currentState = stateList[0]

#open a window, set size
width = 1500
height = 850
size = (width, height)
surface = pygame.display.set_mode(size)

#set title bar of window
pygame.display.set_caption("NewsTree Kiosk")

#color constants
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FUN = (231, 78, 111)
LATTE = (252, 248, 232)

def displayMessage(words, font, fontSize, x, y, color, isUnderlined):
    font = pygame.font.Font(font, fontSize)
    if(isUnderlined):
        font.underline = True
    text = font.render(words, True, color)
    textBounds = text.get_rect()
    textBounds.center = (x, y)
    surface.blit(text, textBounds)


def runStartupSequence():
    currentState = "WELCOME"
    surface.fill(LATTE)
    displayMessage("Welcome to NewsTree", "UnifrakturMaguntia-Regular.ttf", 150, 750, 150, BLACK, False)
    displayMessage("Tap anywhere to continue...", "BricolageGrotesque_24pt-Regular.ttf", 80, 750, 500, BLACK, False)
    
def runNewsList():
    surface.fill(LATTE)
    displayMessage("Tap the Google Chrome banner above", "BricolageGrotesque_24pt-Regular.ttf", 80, 750, 150, BLACK, False)
    displayMessage("or the icon below to continue.", "BricolageGrotesque_24pt-Regular.ttf", 80, 750, 240, BLACK, False)
    pygame.display.update()
    try:
        driver.get("http://68k.news")
        #https://stackoverflow.com/questions/66172852/how-to-un-minimize-selenium-window/66172915#66172915
        handle_of_the_window = driver.current_window_handle
        driver.switch_to.window(handle_of_the_window)
        driver.set_window_rect(0, 0)
        driver.fullscreen_window()
        wait.until(EC.url_changes('http://68k.news/'))
        #https://stackoverflow.com/questions/6460630/close-window-automatically-after-printing-dialog-closes?page=1&tab=scoredesc#tab-top
        driver.execute_script("window.print()")
        driver.execute_script("window.onafterprint = function(){ window.close()}")
        currentState = "PRINT_COMPLETE"
        driver.minimize_window()
        runPrintComplete()
    except Exception as ex2:
        print(type(ex2))
        print("error fetching page")


def runPrintComplete():
    surface.fill(LATTE)
    displayMessage("Thank you for using NewsTree!", "UnifrakturMaguntia-Regular.ttf", 110, 750, 150, BLACK, False)
    displayMessage("Tap anywhere to return to main menu...", "BricolageGrotesque_24pt-Regular.ttf", 75, 750, 500, BLACK, False)
    pygame.display.update()

#---------------------Main Program Loop---------------------

def main():
    global currentState

    while (True):
        if (currentState == "WELCOME"):
            runStartupSequence()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if (currentState == "WELCOME"):
                    runNewsList()
                elif (currentState == "PRINT_COMPLETE"):
                    runStartupSequence()
                else:
                    print(currentState)
                    print("Fatal error. Invalid or unknown state.")
                    pygame.quit()
                    sys.exit(1)

        #update screen
        pygame.display.update()
main()