import pygame

class ground:
    def __init__(self,screen, vit_init = -3):
        self.image = pygame.image.load('sprites/ground/ground.png')
        self.x = 0
        self.rect = pygame.Rect(self.x,screen.get_height()-48,self.image.get_width(),self.image.get_height())
        self.vitesse = vit_init
        

    def update(self):
        self.x += self.vitesse
        if abs(self.x) > 35:
            self.x = 0
         
    def draw(self, screen):
        screen.blit(self.image, (self.x, screen.get_height()-50))
        
    def check_collision(self,bird_rect):
        return (self.rect.colliderect(bird_rect))
