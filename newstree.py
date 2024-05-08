'''
John Reiland

'''

import pygame   #bring in pygame code
import sys #allows closing of pygame window at end of game

#initialize pygame module
pygame.init()

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
print(pygame.font.match_font("amador"))

def displayMessage(words, font, fontSize, x, y, color, isUnderlined):
    font = pygame.font.Font(font, fontSize)
    if(isUnderlined):
        font.underline = True
    text = font.render(words, True, color)
    textBounds = text.get_rect()
    textBounds.center = (x, y)
    surface.blit(text, textBounds)

#---------------------Main Program Loop---------------------

def main():
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()

        #logic goes here
        
        
        #set background color
        surface.fill(LATTE)
        
        #drawing code goes here
        displayMessage("Welcome to NewsTree", "UnifrakturMaguntia-Regular.ttf", 150, 750, 150, BLACK, False)
        displayMessage("Tap anywhere to continue...", "BricolageGrotesque_24pt-Regular.ttf", 80, 750, 500, BLACK, False)

        #update screen
        pygame.display.update()
main()