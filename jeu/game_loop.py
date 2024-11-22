import pygame
from bird import Bird
from pipe import Pipe
from ground import ground
from background import Background
from power_up import Inverse_gravity
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
        # Definition de l'écran
        self.screen = pygame.display.set_mode((width, length))
        self.running = True
        # Definition de l'oiseau
        self.bird = Bird(40, 300, 'basic', length)
        self.clock = pygame.time.Clock()
        # Definition background
        self.background = Background('city')
        # Definition tuyaux
        self.pipes = [Pipe(self.width, random.randint(100, 200), self.length, random.randint(
            100, 300))]  # Générer un tuyau avec une hauteur aléatoire
        self.pipe_spawn_timer = -1500  # Timer pour générer les tuyaux
        # Definition power-ups
        self.powerups = [Inverse_gravity(width, length)]  # Générer un power-up
        # Définit la liste des timers des différents powerups qui vont être pris (11 sec soit 660 frames)
        self.powerups_durations = {self.powerups[0]: 660}
        self.powerups_spawn_timer = -6000  # Timer pour générer les power-ups
        # Apparition fond noir translucide quand on prend un power_up
        self.effet_noir = False
        self.compteur_frames_effet_noir = 0

        # Definition sol
        self.ground = ground(self.screen, 'city')
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

        self.ground.update()  # Met à jour le sol
        for pipe in self.pipes:
            pipe.update_pipe()  # Mettre à jour les tuyaux
        self.background.update()  # Mettre à jour le background
        for powerup in self.powerups:
            powerup.update_powerup(self.length)

        # Générer de nouveaux tuyaux toutes les X millisecondes
        self.pipe_spawn_timer += self.clock.get_time()
        if self.pipe_spawn_timer > 1500:  # Nouveau tuyau toutes les 1.5 secondes
            self.pipes.append(Pipe(self.width, random.randint(
                100, 200), self.length, random.randint(100, 300)))
            self.pipe_spawn_timer = 0

        # Retirer les tuyaux sortis de l'écran
        self.pipes = [pipe for pipe in self.pipes if pipe.x + pipe.width > 0]

        # Génération aléatoire des powerups entre les tuyaux (tous les 8 tuyaux, 30% de chance de faire apparaître un powerup)
        self.powerups_spawn_timer += self.clock.get_time()
        if self.powerups_spawn_timer > 12000 and self.pipe_spawn_timer > 600 and self.pipe_spawn_timer < 800:
            if random.random() > 0.5:
                new_powerup = Inverse_gravity(self.width, self.length)
                self.powerups.append(new_powerup)
                self.powerups_durations[new_powerup] = 660
            self.powerups_spawn_timer = 0

        # Actualiser le timer des powerups actifs
        for powerup in self.powerups:
            if powerup.active:
                self.powerups_durations[powerup] -= 1

        # Retirer les powerups sortis de l'écran ou qui ont leur timer <= 0
        actual_powerups = self.powerups.copy()
        actual_powerups_durations = self.powerups_durations.copy()
        self.powerups = []
        self.powerups_durations = {}
        for powerup in actual_powerups:
            if powerup.x + powerup.rect[2] > 0 and actual_powerups_durations[powerup] > 0:
                self.powerups.append(powerup)
                self.powerups_durations[powerup] = actual_powerups_durations[powerup]
            elif actual_powerups_durations[powerup] <= 0:
                powerup.delete_effect(self.bird)
                powerup.deactivate()
            else:
                powerup.deactivate()

        # Actualiser le compteur d'effet noir si actif
        if self.effet_noir:
            self.compteur_frames_effet_noir += 1
            if self.compteur_frames_effet_noir >= 30:
                self.effet_noir = False
                self.compteur_frames_effet_noir = 0

        # Noircir l'écran si on est proche de perdre un powerup
        for powerup in self.powerups:
            if self.powerups_durations[powerup] == 90:
                self.effet_noir = True
            if self.powerups_durations[powerup] == 30:
                self.effet_noir = True
                pygame.mixer.Sound.play(Powerup_loose_sound)

        self.bird.update()  # Mettre à jour l'oiseau

    def check_collisions(self):
        for pipe in self.pipes:
            if pipe.check_collision(self.bird.rect):  # Si collision avec un tuyau
                self.running = False
                self.effet_noir = False
                self.compteur_frames_effet_noir = 0
        # On vérifie si l'oiseau touche le sol, si c'est le cas il a perdu
        if self.ground.check_collision(self.bird.rect):
            self.running = False
            self.effet_noir = False
            self.compteur_frames_effet_noir = 0

        # Activer les powerups entrés en collision avec l'oiseau
        for powerup in self.powerups:
            if powerup.check_collision(self.bird.rect) and not powerup.active:
                powerup.activate()
                powerup.apply_effect(self.bird)
                pygame.mixer.Sound.play(Powerup_get_sound)
                self.effet_noir = True

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
            for powerup in self.powerups:
                if not powerup.active:
                    pygame.draw.rect(
                        self.screen, (100, 100, 100), powerup.rect, 2)
            pygame.display.flip()

        elif self.check_starting_menu:
            self.screen.blit(self.background.image, (0, 0))
            self.bird.draw(self.screen)
            self.ground.draw(self.screen)
            self.starting_menu.draw(self.screen, (214, 122, 24))
            self.starting_menu.draw_button_back()
            if self.starting_menu.draw_button_back():
                self.background_select += 1
                if self.background_select == len(back)-1:
                    self.background_select = 0
                self.background = Background(back[self.background_select])
                self.ground = ground(self.screen, back[self.background_select])

            if self.starting_menu.draw_button_oiseau():
                self.oiseau_select += 1
                if self.oiseau_select == len(oiseau)-1:
                    self.oiseau_select = 0
                self.bird = Bird(
                    40, 300, oiseau[self.oiseau_select], self.length)
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

            for pipe in self.pipes:
                pipe.display_pipe(self.screen)  # Dessiner les tuyaux
            self.ground.draw(self.screen)  # Dessine le sol
            for powerup in self.powerups:
                powerup.draw_powerup(self.screen)
            draw_text(str(self.score), pygame.font.SysFont(
                'bauhaus93', 60), (255, 255, 255), int(self.width/2), 20, self.screen)
            if self.effet_noir:
                self.screen.blit(pygame.image.load(
                    'Backgrounds/noir_powerup.png'), (0, 0))
            self.bird.draw(self.screen)  # Dessiner l'oiseau
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
                40, 300, oiseau[self.oiseau_select], self.length)
            self.pipes = []
            self.pipe_spawn_timer = 0
            self.powerups = []
            self.powerups_durations = {}
            self.powerups_spawn_timer = -500
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
Flap_sound.set_volume(0.7)
Powerup_get_sound = pygame.mixer.Sound("son/powerup_get.mp3")
Powerup_get_sound.set_volume(0.99)
Powerup_loose_sound = pygame.mixer.Sound("son/powerup_loose.mp3")
Powerup_loose_sound.set_volume(0.99)
pygame.mixer.music.load("son/musique.wav")
pygame.mixer.music.set_volume(0.3)

# Lancer le jeu
game = Game(900, 520)
game.run()
