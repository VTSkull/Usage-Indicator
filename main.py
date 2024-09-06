from cpu import *
from gpu import *
from ram import *
import pygame

pygame.init()
width = 500
height = 500

screen = pygame.display.set_mode((width, height))

colorBlock = pygame.Rect((0, 0, 500, 500))

"""
100% = 255 0 0
50% = 255 255 0
0% = 0 255 0

"""

run = True
while run:
    #percentage = GPU().LoadPercent()
    percentage = RAM().Percent()
    percentage = percentage / 100
    if percentage < 0.5:
        green = ((255 - 0) * (1 - percentage)) + 0
    else:
        green = ((0 - 255) * percentage) + 255

    red = ((255 - 0) * percentage) + 0
    #red = int(round(red, 0))

    pygame.draw.rect(screen, (red, green, 0), colorBlock)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
