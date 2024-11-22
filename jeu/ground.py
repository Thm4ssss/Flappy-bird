import pygame


class ground:
    def __init__(self, screen, theme, vit_init=-3):
        if theme == 'jungle':
            self.image = pygame.image.load('sprites/ground/ground_jungle.png')
        elif theme == 'city':
            self.image = pygame.image.load('sprites/ground/ground_city.png')
        elif theme == 'desert':
            self.image = pygame.image.load('sprites/ground/ground_desert.png')
        elif theme == 'volcan':
            self.image = pygame.image.load('sprites/ground/ground_volcan.png')
        elif theme == 'usine':
            self.image = pygame.image.load('sprites/ground/ground_usine.png')
        else:
            self.image = pygame.image.load('sprites/ground/ground.png')
        self.x = 0
        self.rect = pygame.Rect(self.x, screen.get_height(
        )-48, self.image.get_width(), self.image.get_height())
        self.vitesse = vit_init

    def update(self):
        self.x += self.vitesse
        if abs(self.x) > 35:
            self.x = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, screen.get_height()-50))

    def check_collision(self, bird_rect):
        return (self.rect.colliderect(bird_rect))
