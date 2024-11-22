import pygame
import random as rd
from abc import ABC, abstractmethod


class PowerUp(ABC):
    def __init__(self, screen_width, screen_height):
        self.x = screen_width
        self.speed = 3
        self.min_y = screen_height/2 - 100
        self.max_y = screen_height/2 + 100
        self.y = rd.randint(int(self.min_y)+1, int(self.max_y))
        self.vertical_speed = 2  # Vitesse du mouvement vertical
        self.direction = 1  # 1 pour descendre, -1 pour monter
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
            self.index = (self.index + 1) % len(self.images)
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

    def speed_up(self):
        self.speed = 4

    def speed_down(self):
        self.speed = 3

    @abstractmethod
    def apply_effect(self, bird, pipes_list, powerups_list):
        pass

    @abstractmethod
    def delete_effect(self, bird, pipes_list, powerups_list):
        pass


class Inverse_gravity(PowerUp):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.images = [pygame.image.load(
            './sprites/Reverse/reverse' + str(i) + '.png') for i in range(0, 80)]
        # définition de la hitbox
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def apply_effect(self, bird, pipes_list, powerups_list):
        bird.apply_gravity_inversion()

    def delete_effect(self, bird, pipes_list, powerups_list):
        bird.apply_gravity_inversion()


class Acceleration(PowerUp):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.images = [pygame.transform.scale(pygame.image.load(
            './sprites/Rocket/31b7380512be4334a997ef5ceea3ed46bmQE3MpTKfGDrdx3-' + str(i) + '.png'), (60, 60)) for i in range(0, 48)]
        # définition de la hitbox
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def apply_effect(self, bird, pipes_list, powerups_list):
        for pipe in pipes_list:
            pipe.speed_up()
        for powerup in powerups_list:
            powerup.speed_up()

    def delete_effect(self, bird, pipes_list, powerups_list):
        for pipe in pipes_list:
            pipe.speed_down()
        for powerup in powerups_list:
            powerup.speed_down()
