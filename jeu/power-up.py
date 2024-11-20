import pygame
import random
from abc import ABC
from game_loop import inverse_gravity

"""class Powerup:
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
        self.active = False"""

class PowerUp(ABC):
    def __init__(self, screen_width, screen_height, height,image_path ):
        self.x=screen_width
        self.y=0
        self.speed=3
        self.height=height
        self.image=pygame.transform.scale(image_path,(90,self.height))
        self.width=self.image.get_width()

        #définition de la hitbox
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
    
    def update_powerup(self):
        # Déplacement horizontal du powerup
        self.x -= self.speed

        # Mise à jour de la hitbox du powerup pour suivre son déplacement
        self.rect.x = self.x
    
    def check_collision(self, bird_rect):
        # On regarde si la hitbox de l'oiseau est entrée en collision avec celle du powerup ou non
        return self.rect.colliderect(bird_rect) 

    def display_powerup(self, screen):
        # On affiche les powerup
        screen.blit(self.image, (self.x, self.y))
    

    @abstractmethod
    def apply_effect(self):
        pass
        
class anti_gravity(PowerUp):
    def __init__(self, screen_width, screen_height, height, image):
        super.__init__(screen_width, screen_height, height, image)
    
    def apply_effect(self):
        # Inverser la gravité de l'oiseau
        inverse_gravity()

