import pygame
from bird import Bird
from pipe import Pipe
from ground import ground
from background import Background
from score import draw_text, Button
from starting_menu import Starting_menu
import random
from restart_menu import Restart_menu

back = ['city', 'jungle', 'volcan', 'desert', 'usine', -1]
oiseau = ['basic', 'angry', 'rapide', -1]


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
        self.ground = ground(self.screen, 'city')  # Importe le sol
        self.dev = False   # Mode Développeur
        self.window_is_active = True
        self.score = 0  # Initialisation du score
        self.pass_pipe = False  # Vérification de passage de tuyaux pour calcul de score
        self.check_starting_menu = False
        self.starting_menu = Starting_menu(self.screen)
        self.background_select = 0
        self.oiseau_select = 0
        self.game_over = False
        self.restart_menu = Restart_menu(self.screen)

    # Permet la gestion des intéractions entre l'utilisateur et le jeu
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window_is_active = False
                pygame.mixer.music.stop()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.start_game:
                        self.start_game = True
                    else:
                        self.bird.flap()
                        pygame.mixer.Sound.play(Flap_sound)
        if self.game_over:
            if self.restart_menu.restart_button.draw():
                self.game_over = False
            elif self.restart_menu.quit_button.draw():
                self.window_is_active = False
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
                self.running = False
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

        elif self.check_starting_menu:
            self.screen.blit(self.background.image, (0, 0))
            self.bird.draw(self.screen)
            self.ground.draw(self.screen)
            self.starting_menu.draw(self.screen,(214, 122, 24))
            if self.starting_menu.draw_button_back():
                self.background_select +=1
                if self.background_select == len(back):
                    self.background_select=0
                self.background = Background(back[self.background_select])

            if self.starting_menu.draw_button_oiseau():
                self.oiseau_select +=1
                if self.oiseau_select == len(oiseau):
                    self.oiseau_select=0
                self.bird = Bird(40, 300, oiseau[self.oiseau_select], 0.5, self.length)
            pygame.display.flip()
        elif self.game_over:
            self.screen.blit(self.background.image, (0, 0))  # Dessiner le fond
            self.bird.draw(self.screen)  # Dessiner l'oiseau
            for pipe in self.pipes:
                pipe.display_pipe(self.screen)  # Dessiner les tuyaux
            self.ground.draw(self.screen)  # Dessine le sol
            self.restart_menu.display_restart_menu()
            draw_text("Score: "+str(self.score), pygame.font.SysFont(
                'bauhaus93', 60), (255, 255, 255), int(self.width/2)-pygame.font.SysFont(
                'bauhaus93', 60).render("Score: "+str(self.score), True, (255, 255, 255)).get_width()/2, (self.length/2)-50, self.screen)
            pygame.display.flip()

        else:
            self.screen.blit(self.background.image, (0, 0))  # Dessiner le fond
            self.bird.draw(self.screen)  # Dessiner l'oiseau
            for pipe in self.pipes:
                pipe.display_pipe(self.screen)  # Dessiner les tuyaux
            self.ground.draw(self.screen)  # Dessine le sol
            draw_text(str(self.score), pygame.font.SysFont(
                'bauhaus93', 60), (255, 255, 255), int(self.width/2), 20, self.screen)
            pygame.display.flip()

    def update_score(self):
        if len(self.pipes) > 0:
            if self.bird.rect.x > self.pipes[0].x and self.bird.rect.x < self.pipes[0].x + self.pipes[0].width and self.pass_pipe == False:
                self.pass_pipe = True
            if self.pass_pipe == True:
                if self.bird.rect[0] >= self.pipes[0].x + self.pipes[0].width:
                    self.score += 1
                    self.pass_pipe = False

    def run(self):
        while self.window_is_active:
            self.running = True
            self.start_game = False
            self.game_over = False
            self.bird = Bird(
                40, 300, oiseau[self.oiseau_select], 0.5, self.length)
            self.pipes = []
            self.pipe_spawn_timer = 0
            self.score = 0
            while self.start_game == False and self.window_is_active:
                self.handling_events()
                self.check_starting_menu = True
                self.display()
            while self.running and self.window_is_active:
                self.check_starting_menu = False
                self.clock.tick(60)  # Limiter à 60 FPS
                self.handling_events()  # Gestion des événements
                self.update()  # Mise à jour des objets
                self.update_score()
                self.check_collisions()  # Vérification des collisions
                self.display()  # Affichage à l'écran
            self.game_over = True
            while self.game_over and self.window_is_active:
                self.handling_events()
                self.display()

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
