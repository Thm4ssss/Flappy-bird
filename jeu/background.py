import pygame


class Background():
    def __init__(self, theme):
        self.index = 0
        if theme == 'jungle':
            self.frames = [pygame.transform.scale(pygame.image.load(
                "./Backgrounds/fond_jungle/642d6d07-391c-4d40-b591-f63836213a92-" + str(i) + ".png").convert(), (950, 520)) for i in range(0, 300)]

        elif theme == 'city':
            self.frames = [pygame.transform.scale(pygame.image.load(
                "./Backgrounds/fond_city/c2896587-f7f6-4ec2-9904-6514eee66992-" + str(i) + ".png").convert(), (950, 520)) for i in range(0, 359)]

        elif theme == 'volcan':
            self.frames = [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_volcan/8294d897c07847f9cda1f87ad245edfdPIi6qW7MxBWez3sj-" + str(i) + ".png").convert(), (950, 520)) for i in range(
                0, 300)] + [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_volcan/313ff144c8094719bc674831be8ae13bqmSUahg2UES8P9yy-" + str(i) + ".png").convert(), (950, 520)) for i in range(0, 294)]

        elif theme == 'desert':
            self.frames = [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_desert/e8ba8d5175db4071c5327adece83b56f3Qbzul3a7jgnynw4-" + str(i) + ".png").convert(), (950, 520)) for i in range(
                0, 300)] + [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_desert/fc43c078068246c0d5e02798ee2595b9gQLSHKrn0HPy5AKz-" + str(i) + ".png").convert(), (950, 520)) for i in range(0, 300)]

        elif theme == 'usine':
            self.frames = [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_usine/5a1f845c9be14088d2242bcb954995ccdIGDpvTc5BE0vmia-" + str(i) + ".png").convert(), (950, 520)) for i in range(
                0, 304)] + [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_usine/a973ea7540414e82cba8b838bd3e3d92gaDKDhmKvEmNLxKm-32" + str(i) + ".png").convert(), (950, 520)) for i in range(4, 35)]

        else:
            self.frames = [pygame.transform.scale(pygame.image.load(
                "./Backgrounds/fond_base").convert(), (950, 520))]

        self.image = self.frames[self.index]
        self.compteur = 0

    def update(self):
        self.compteur += 1
        if self.compteur == 3:
            self.compteur = 0
            self.index = (self.index + 1) % len(self.frames)
        self.image = self.frames[self.index]
