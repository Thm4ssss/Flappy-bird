import pygame
import random as rd

fps = 60


class Bird():
    def __init__(self, x, y, image1, image2, image3, image4, gravity,screen_height):
        self.images = [pygame.image.load(
            image1), pygame.image.load(image2), pygame.image.load(image3), pygame.image.load(image4)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.movement = 0
        self.gravity = 30*gravity/fps
        self.height=screen_height

    # pour réinitialiser la position de l'oiseau si jamais on le réutilise 2 fois d'affilée
    def reset(self, x, y):
        self.rect.center = (x, y)
        self.movement = 0
        self.index = 0
        self.image = self.images[self.index]
            
    # gère les sauts
    def flap(self):
        if self.rect.top>=10*30/fps:
            self.movement = -10*30/fps
        else:
            self.movement=0

    # rotation de l'oiseau en fonction de sa vitesse de chute
    def rotate(self):
        # Limiter l'angle de rotation pour éviter des rotations excessives
        max_rotation = 25
        min_rotation = -90
        rotation_angle = max(
            min(self.movement * -2, max_rotation), min_rotation)
        self.image = pygame.transform.rotozoom(
            self.images[self.index], rotation_angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    
    # gère l'animation de l'oiseau et la chute à chaque instant
    def update(self):
        self.movement += self.gravity
        self.rect.y += self.movement
        tirage = rd.random()
        if tirage > 0.5:
            self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]
        self.rotate()

    # afficher l'oiseau sur l'écran
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))


'''
Exemple de création d'un oiseau

Oiseau standard :
bird = Bird(40, 300, './sprites/bird_base/bird_base1.png', './sprites/bird_base/bird_base2.png',
            './sprites/bird_base/bird_base3.png', './sprites/bird_base/bird_base4.png', 0.5)


'''
