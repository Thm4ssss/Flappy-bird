import random as rd
import pygame


fps = 60


class Bird():
    def __init__(self, x, y, type_oiseau, screen_height):
        # Chaque oiseau a un skin et un poids différent
        if type_oiseau == 'basic':
            self.images = [pygame.image.load('./sprites/bird_base/bird_base1.png'), pygame.image.load('./sprites/bird_base/bird_base2.png'),
                           pygame.image.load('./sprites/bird_base/bird_base3.png'), pygame.image.load('./sprites/bird_base/bird_base4.png')]
            self.poids = 0.5
        elif type_oiseau == 'angry':
            self.images = [pygame.image.load(
                './sprites/bird_angry/bird_angry' + str(i) + '.png') for i in range(1, 5)]
            self.poids = 0.6
        elif type_oiseau == 'rapide':
            self.images = [pygame.image.load(
                './sprites/bird_rapide/bird_rapide' + str(i) + '.png') for i in range(1, 5)]
            self.poids = 0.4
        else:
            self.images = [pygame.image.load(
                './sprites/cat/cat' + str(i) + '.png') for i in range(1, 5)]
            self.poids = 0.5

        self.compteur = 0       # on ne change pas l'image de l'oiseau pour l'animer à chaque frame

        # Définitions liées aux sprites
        # Images
        self.index = 0
        self.image = self.images[self.index]
        # Hitboxes
        self.rect = self.image.get_rect(center=(x, y))
        # Définitions liées au mouvement de l'oiseau
        self.movement = 0
        self.coeff_grav = 1
        self.gravity = 30*self.coeff_grav*self.poids/fps
        self.jump_strength = 10 * 30 / fps  # Force du saut

        self.height = screen_height

    # pour réinitialiser la position de l'oiseau si jamais on le réutilise 2 fois d'affilée
    def reset(self, x, y):
        self.rect.center = (x, y)
        self.movement = 0
        self.index = 0
        self.image = self.images[self.index]

    # gère les sauts
    def flap(self):
        if self.coeff_grav > 0:
            if self.rect.top > self.jump_strength:
                self.movement = - self.jump_strength
            else:
                self.movement = 0
        else:
            self.movement = self.jump_strength

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
        # mouvement vertical
        if self.coeff_grav < 0 and self.rect.top < self.gravity:
            pass
        else:
            self.movement += self.gravity
            self.rect.y += self.movement

        # animation oiseau
        self.compteur += 1
        if self.compteur == 3:
            self.index = (self.index + 1) % len(self.images)
            self.compteur = 0
        self.image = self.images[self.index]

       # flip de l'image si la gravité est inversée
        self.image = pygame.transform.flip(self.image, False, True)

        # rotation + remettre l'image à l'endroit si la gravité est normale
        if self.coeff_grav > 0:
            self.rotate()

    # afficher l'oiseau sur l'écran
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # fonction liée au powerup de changement de gravité
    def apply_gravity_inversion(self):
        self.coeff_grav *= -1
        self.gravity = 30*self.coeff_grav*self.poids/fps
        self.movement = 0
