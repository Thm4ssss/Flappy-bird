import pygame
running=True
while running:
    screen=pygame.display.set_mode((800,600))
    for event in pygame.event.get():
        if event==quit:
            running=False
    