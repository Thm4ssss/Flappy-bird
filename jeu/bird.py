import sys
import pygame


class Bird():
    def __init__(self, x, y, image1, image2):
        self.images = [pygame.image.load(
            'image1'), pygame.image.load('image2')]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.movement = 0
        self.gravity = 0.5

    def flap(self):
        self.movement = -10

    def update(self):
        self.movement += self.gravity
        self.rect.y += self.movement
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]

    def draw(self, screen):
        screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

bird = Bird(50, 300, )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()

    bird.update()

    screen.fill((0, 0, 0))  # Effacer l'écran
    bird.draw(screen)  # Dessiner l'oiseau

    pygame.display.update()
    clock.tick(30)
