import pygame
import random


class Powerup:
    def __init__(self, x, y, duration):
        self.image = pygame.image.load('powerup.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.active = True
        self.duration = duration
        self.start_time = None

    def apply(self, bird):
        pass  # Cette méthode sera redéfinie dans les sous-classes

    def update(self):
        self.rect.x -= 3  # Déplacement du power-up vers la gauche
        if self.start_time and pygame.time.get_ticks() - self.start_time > self.duration:
            self.deactivate(bird)

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.rect)

    def activate(self, bird):
        self.start_time = pygame.time.get_ticks()
        self.apply(bird)

    def deactivate(self, bird):
        self.active = False
