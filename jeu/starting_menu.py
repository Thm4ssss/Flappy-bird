import pygame
from score import draw_text,Button

restart_img = pygame.image.load('sprites/buttons/restart.png')
restart_hovered_img = pygame.image.load('sprites/buttons/restart_hovered.png')

class Starting_menu():
    def __init__(self,screen):
      self.Button_oiseau = Button(screen.get_width()/2-60,200,restart_img,restart_hovered_img,screen)
      self.Button_back = Button(screen.get_width()/2-60,300,restart_img,restart_hovered_img,screen)
      
    def draw(self,screen,couleur):
        screen.blit(pygame.font.Font('police/Sabo-Regular.otf', 50).render('Floppy Bird',True,couleur),(screen.get_width()/2-pygame.font.Font('police/Sabo-Regular.otf', 50).render('Floppy Bird',True,couleur).get_width()/2,50))
        screen.blit(pygame.font.Font('police/Sabo-Regular.otf', 30).render('Press scpace-bar to play',True,(255,255,255)),(screen.get_width()/2-pygame.font.Font('police/Sabo-Regular.otf', 30).render('Press scpace-bar to play',True,(255,255,255)).get_width()/2,400))
        
    def draw_button_oiseau(self):
        return self.Button_oiseau.draw()
    
    def draw_button_back(self):
        return self.Button_back.draw()
 