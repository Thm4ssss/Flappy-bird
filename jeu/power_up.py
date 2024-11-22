import pygame
import random as rd
from abc import ABC, abstractmethod


class PowerUp(ABC):
    def __init__(self, screen_width, screen_height):
        self.x = screen_width
        self.y = screen_height/2
        self.speed = 3
        self.min_y = screen_height/2 - 100
        self.max_y = screen_height/2 + 100
        self.vertical_speed = 2  # Vitesse du mouvement vertical
        self.direction = 1  # 1 pour descendre, -1 pour monter
        self.compteur = 0
        self.index = 0
        self.images = [pygame.image.load('./sprites/Reverse/reverse1.png')]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.active = False

    def update_powerup(self, screen_height):
        if not self.active:
            # Déplacement horizontal du powerup
            self.x -= self.speed
            self.rect.x -= self.speed
            # Changement de l'image dans l'animation du power-up
            self.compteur += 1
            if self.compteur == 60:
                self.index = (self.index + 1) % len(self.images)
                self.compteur = 0
            self.image = self.images[self.index]
        # Déplacement vertical du powerup
            self.y += self.vertical_speed * self.direction
            self.rect.y = self.y

            # Inverser la direction si les limites sont atteintes
            if self.y <= self.min_y or self.y >= self.max_y:
                self.direction *= -1

    def check_collision(self, bird_rect):
        # On regarde si la hitbox de l'oiseau est entrée en collision avec celle du powerup ou non
        return self.rect.colliderect(bird_rect)

    def draw_powerup(self, screen):
        if not self.active:
            # On affiche les powerup
            screen.blit(self.image, (self.x, self.y))

    # Activation de l'effet
    def activate(self):
        self.active = True

    # Desactivation de l'effet
    def deactivate(self):
        self.active = False

    @abstractmethod
    def apply_effect(self, bird):
        pass

    @abstractmethod
    def delete_effect(self, bird):
        pass


class Inverse_gravity(PowerUp):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.images = [pygame.image.load(
            './sprites/Reverse/reverse' + str(i) + '.png') for i in range(1, 5)]
        # définition de la hitbox
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def apply_effect(self, bird):
        bird.apply_gravity_inversion()

    def delete_effect(self, bird):
        bird.apply_gravity_inversion()
