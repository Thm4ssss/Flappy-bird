import pygame
from bird import Bird
from pipe import Pipe
import random


class Game:
    # Constructeur de la classe game, permet de définir toutes les variables utiles au bon fonctionnement du jeu
    def __init__(self, width, length):
        pygame.init()
        self.width = width
        self.length = length
        self.screen = pygame.display.set_mode((width, length))
        self.running = True
        self.bird = Bird(40, 300, './sprites/bird_base/bird_base1.png', './sprites/bird_base/bird_base2.png',
                         './sprites/bird_base/bird_base3.png', './sprites/bird_base/bird_base4.png', 0.5, length)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("Backgrounds/fond_base.png").convert()
        self.pipes = [Pipe(self.width, random.randint(100,200),self.length,random.randint(100,300))]  # Générer un tuyau avec une hauteur aléatoire
        self.pipe_spawn_timer = 0  # Timer pour générer les tuyaux

    # Permet la gestion des intéractions entre l'utilisateur et le jeu
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()

    # Permet la mise à jour des différents éléments du jeu
    def update(self):
        self.bird.update()  # Mettre à jour l'oiseau
        for pipe in self.pipes:
            pipe.update_pipe()  # Mettre à jour les tuyaux

        # Retirer les tuyaux sortis de l'écran
        self.pipes = [pipe for pipe in self.pipes if pipe.x + pipe.width > 0]

        # Générer de nouveaux tuyaux toutes les X millisecondes
        self.pipe_spawn_timer += self.clock.get_time()
        if self.pipe_spawn_timer > 1500:  # Nouveau tuyau toutes les 1.5 secondes
            self.pipes.append(Pipe(self.width, random.randint(100, 200),self.length,random.randint(100,300)))
            self.pipe_spawn_timer = 0
 
    def check_collisions(self):
        for pipe in self.pipes:
            if pipe.check_collision(self.bird.rect):  # Si collision avec un tuyau
                self.running = False
        # On vérifie si l'oiseau touche le sol, si c'est le cas il a perdu
        if self.bird.rect.bottom >= self.length:
            self.running = False

    def display(self):
        self.screen.blit(self.background, (0, 0))  # Dessiner le fond
        self.bird.draw(self.screen)  # Dessiner l'oiseau
        for pipe in self.pipes:
            pipe.display_pipe(self.screen)  # Dessiner les tuyaux
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(60)  # Limiter à 60 FPS
            self.handling_events()  # Gestion des événements
            self.update()  # Mise à jour des objets
            self.check_collisions()  # Vérification des collisions
            self.display()  # Affichage à l'écran
        pygame.quit()


# Lancer le jeu
game = Game(950, 520)
game.run()
