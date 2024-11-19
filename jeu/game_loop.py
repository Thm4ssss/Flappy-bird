import pygame
from bird import Bird
from pipe import Pipe
from ground import ground
from background import Background
import random

class Game:
    # Constructeur de la classe game, permet de définir toutes les variables utiles au bon fonctionnement du jeu
    def __init__(self, width, length):
        pygame.init()
        pygame.mixer.music.play(- 1)
        self.width = width
        self.length = length
        self.screen = pygame.display.set_mode((width, length))
        self.running = True
        self.bird = Bird(40, 300, 'basic', 0.5, length)
        self.clock = pygame.time.Clock()
        self.background = Background('city')
        self.pipes = [Pipe(self.width, random.randint(100, 200), self.length, random.randint(
            100, 300))]  # Générer un tuyau avec une hauteur aléatoire
        self.pipe_spawn_timer = -1500  # Timer pour générer les tuyaux
        self.ground = ground(self.screen)  # Importe le sol
        self.dev = False
        self.window_is_active=True

    # Permet la gestion des intéractions entre l'utilisateur et le jeu
    def handling_events(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT: 
                self.window_is_active = False
                pygame.mixer.music.stop()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.start_game:
                        self.start_game=True
                    else:
                        self.bird.flap()
                        pygame.mixer.Sound.play(Flap_sound)
                        

    # Permet la mise à jour des différents éléments du jeu
    def update(self):
        self.bird.update()  # Mettre à jour l'oiseau
        self.ground.update()  # Met à jour le sol
        for pipe in self.pipes:
            pipe.update_pipe()  # Mettre à jour les tuyaux
        self.background.update()  # Mettre à jour le background
        # Retirer les tuyaux sortis de l'écran
        self.pipes = [pipe for pipe in self.pipes if pipe.x + pipe.width > 0]

        # Générer de nouveaux tuyaux toutes les X millisecondes
        self.pipe_spawn_timer += self.clock.get_time()
        if self.pipe_spawn_timer > 1500:  # Nouveau tuyau toutes les 1.5 secondes
            self.pipes.append(Pipe(self.width, random.randint(
                100, 200), self.length, random.randint(100, 300)))
            self.pipe_spawn_timer = 0

    def check_collisions(self):
        for pipe in self.pipes:
            if pipe.check_collision(self.bird.rect):  # Si collision avec un tuyau
                self.running=False
        # On vérifie si l'oiseau touche le sol, si c'est le cas il a perdu
        if self.ground.check_collision(self.bird.rect):
            self.running = False

    def display(self):
        if self.dev:
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (255, 0, 0), self.bird.rect, 2)
            pygame.draw.rect(self.screen, (255, 255, 0), self.ground.rect, 2)
            for pipe in self.pipes:
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 pipe.top_rect, 2)
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 pipe.bottom_rect, 2)
            pygame.display.flip()
        else:
            self.screen.blit(self.background.image, (0, 0))  # Dessiner le fond
            self.bird.draw(self.screen)  # Dessiner l'oiseau
            for pipe in self.pipes:
                pipe.display_pipe(self.screen)  # Dessiner les tuyaux
            self.ground.draw(self.screen)  # Dessine le sol
            pygame.display.flip()

    def run(self):
        while self.window_is_active:
            self.running = True
            self.start_game = False
            self.bird = Bird(40, 300,"basic", 0.5, self.length)
            self.pipes = []
            self.pipe_spawn_timer = 0
            while self.start_game==False and self.window_is_active:
                    self.handling_events()
                    self.display()
            while self.running and self.window_is_active:
                self.clock.tick(60)  # Limiter à 60 FPS
                self.handling_events()  # Gestion des événements
                self.update()  # Mise à jour des objets
                self.check_collisions()  # Vérification des collisions
                self.display()  # Affichage à l'écran    
        pygame.quit()


# Ajout de la musque
pygame.mixer.init()
Flap_sound = pygame.mixer.Sound("son/Flap.wav")
Flap_sound.set_volume(0.99)
pygame.mixer.music.load("son/musique.wav")
pygame.mixer.music.set_volume(0.3)

# Lancer le jeu
game = Game(900, 520)
game.run()
