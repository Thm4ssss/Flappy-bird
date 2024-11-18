import pygame
import random as rd

image_tuyau_haut = pygame.image.load("tuyau_haut.png")
image_tuyau_bas = pygame.image.load("tuyau_bas.png")
    
class Pipe:
    def __init__(self,screen_width,gap,image_top=image_tuyau_haut,image_bottom=image_tuyau_bas):
        #Définition des variables utiles d'un tuyau, tel que la position (coin haut gauche, la vitesse de déplacement ou encore l'écart entre deux tuyaux)
        self.x=screen_width
        self.y=0
        self.speed=-3
        self.gap=gap
        self.image_top=image_top
        self.image_bottom=image_bottom
        self.width=image_top.get_width()
        self.height=image_top.get_height()
        
        #Définition de la hitbox
        self.top_rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.bottom_rect=pygame.Rect(self.x,self.y+self.gap,self.width,900)
        
    def update_pipe(self):
        #Déplacement horizontal du tuyau
        self.x-=self.speed
        
        #Mise à jour de la hitbox du tuyau pour suivre son déplacement
        self.top_rect.x=self.x
        self.bottom_rect.x=self.x
    
    def check_collision(self,bird_rect):
        #On regarde si la hitbox de l'oiseau est entrée en collision avec celle du tuyau ou non
        return (self.top_rect.colliderect(bird_rect) or self.bottom_rect.colliderect(bird_rect))