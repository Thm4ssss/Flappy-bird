import pygame


class Background():
    def __init__(self, theme):
        self.index = 0
        self.theme=theme
        if theme == 'jungle':
            self.frames = [pygame.transform.scale(pygame.image.load(
                "./Backgrounds/fond_jungle/642d6d07-391c-4d40-b591-f63836213a92-" + str(i) + ".png").convert(), (950, 520)) for i in range(0, 300)]

        elif theme == 'city':
            self.frames = [pygame.transform.scale(pygame.image.load(
                "./Backgrounds/fond_city/c2896587-f7f6-4ec2-9904-6514eee66992-" + str(i) + ".png").convert(), (950, 520)) for i in range(0, 359)]

        elif theme == 'volcan':
            self.frames = [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_volcan/d598f7a2-77bd-49fb-a7de-a6415a0647a8-" + str(i) + ".png").convert(), (950, 520)) for i in range(
                0, 300)] + [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_volcan/c679c560-7154-4124-ae70-6626c9a53e12-" + str(i) + ".png").convert(), (950, 520)) for i in range(0, 294)]

        elif theme == 'desert':
            self.frames = [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_desert/2279c49d1d1143419e53e5a67e87eb07Vu9z7CDdIDkLMri1-" + str(i) + ".png").convert(), (950, 520)) for i in range(
                0, 300)] + [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_desert/6bce98ab34934318b1fb4c768f12d549N7J5qwMGldlWyy61-" + str(i) + ".png").convert(), (950, 520)) for i in range(0, 300)]

        elif theme == 'usine':
            self.frames = [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_usine/5a1f845c9be14088d2242bcb954995ccdIGDpvTc5BE0vmia-" + str(i) + ".png").convert(), (950, 520)) for i in range(
                0, 304)] + [pygame.transform.scale(pygame.image.load("./Backgrounds/fond_usine/a973ea7540414e82cba8b838bd3e3d92gaDKDhmKvEmNLxKm-" + str(i) + ".png").convert(), (950, 520)) for i in range(4, 35)]

        else:
            self.frames = [pygame.transform.scale(pygame.image.load(
                "./Backgrounds/fond_base.png").convert(), (950, 520))]

        self.image = self.frames[self.index]
        self.compteur = 0

    def update(self):
        self.compteur += 1
        if self.compteur == 3:
            self.compteur = 0
            self.index = (self.index + 1) % len(self.frames)
        self.image = self.frames[self.index]
