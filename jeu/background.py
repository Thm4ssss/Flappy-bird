import pygame


class Background():
    def __init__(self, environnement):
        self.index = 0
        if environnement == 'jungle':
            self.frames = [pygame.transform.scale(pygame.image.load(
                "./Backgrounds/fond_jungle/642d6d07-391c-4d40-b591-f63836213a92-" + str(i) + ".png").convert(), (950, 520)) for i in range(0, 300)]

        if environnement == 'city':
            self.frames = [pygame.transform.scale(pygame.image.load(
                "./Backgrounds/fond_city/c2896587-f7f6-4ec2-9904-6514eee66992-" + str(i) + ".png").convert(), (950, 520)) for i in range(0, 359)]

        self.image = self.frames[self.index]
        self.compteur = 0

    def update(self):
        self.compteur += 1
        if self.compteur == 2:
            self.compteur = 0
            self.index = (self.index + 1) % len(self.frames)
        self.image = self.frames[self.index]
