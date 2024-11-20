import pygame
from score import draw_text,Button


class Starting_menu():
    def __init__(self):
      self.x=0  
      
    def draw(self,screen,couleur):
        screen.blit(pygame.font.Font('police/Sabo-Regular.otf', 50).render('Floppy Bird',True,couleur),(screen.get_width()/2-pygame.font.Font('police/Sabo-Regular.otf', 50).render('Floppy Bird',True,couleur).get_width()/2,50))
        screen.blit(pygame.font.Font('police/Sabo-Regular.otf', 30).render('Press scpace-bar to play',True,(255,255,255)),(screen.get_width()/2-pygame.font.Font('police/Sabo-Regular.otf', 30).render('Press scpace-bar to play',True,(255,255,255)).get_width()/2,400))
        
