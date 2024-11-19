import pygame
import random as rd

image_tuyau_haut = pygame.image.load("./sprites/tuyaux/image_tuyau_haut.png")
image_tuyau_bas = pygame.image.load("./sprites/tuyaux/image_tuyau_bas.png")


class Pipe:
    def __init__(self,screen_width,gap,screen_height,top_pipe_height,image_top=image_tuyau_haut,image_bottom=image_tuyau_bas):
        #Définition des variables utiles d'un tuyau, tel que la position (coin haut gauche, la vitesse de déplacement ou encore l'écart entre deux tuyaux)
        self.x=screen_width
        self.y=0
        self.speed=3
        self.gap=gap
        self.top_height=top_pipe_height
        self.bottom_height=screen_height-self.top_height-self.gap
        self.image_top=pygame.transform.scale(image_top,(90,self.top_height))
        self.image_bottom=pygame.transform.scale(image_bottom,(90,self.bottom_height))
        self.width=self.image_top.get_width()
        
        
        #Définition de la hitbox
        self.top_rect=pygame.Rect(self.x,self.y,self.width,self.top_height)
        self.bottom_rect=pygame.Rect(self.x,self.top_height+self.gap,self.width,self.bottom_height)
        
    def update_pipe(self):
        # Déplacement horizontal du tuyau
        self.x -= self.speed

        # Mise à jour de la hitbox du tuyau pour suivre son déplacement
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def check_collision(self, bird_rect):
        # On regarde si la hitbox de l'oiseau est entrée en collision avec celle du tuyau ou non
        return (self.top_rect.colliderect(bird_rect) or self.bottom_rect.colliderect(bird_rect))

    def display_pipe(self, screen):
        # On affiche les tuyaux
        screen.blit(self.image_top, (self.x, self.y))
        screen.blit(self.image_bottom, (self.x, self.top_height+self.gap))
