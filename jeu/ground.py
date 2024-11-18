import pygame

class ground():
    def __init__(self,vit_init = -4):
        self.image = pygame.image.load('sprites/ground.png')
        self.rect = self.image.get_rect()
        self.vitesse = vit_init
        self.x = 0

    def update(self):
        self.x += self.vitesse
        if abs(self.x) > 35:
		    self.x = 0
         
    def draw(self, screen):
        screen.blit(self.image, (self.x, screen.get_height()-20))
        
    def check_collision(self,bird_rect):
        return (self.rect.colliderect(bird_rect))
