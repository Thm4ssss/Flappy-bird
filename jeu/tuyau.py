import pygame
import random

image_tuyau_haut = pygame.image.load("tuyau_haut.png")
image_tuyau_bas = pygame.image.load("tuyau_bas.png")
    
class Tuyau:
    def __init__(self,largeur_fenetre):
            self.largeur = image_tuyau_haut.get_width()
            self.hauteur = random.randint(150, 450)
            self.espace = 200
            self.vitesse = -3
            self.x = largeur_fenetre

    def mettre_a_jour(self,largeur_fenetre):
        self.x += self.vitesse
        if self.x < -self.largeur:
            self.x = largeur_fenetre
            self.hauteur = random.randint(150, 450)

    def dessiner(self, fenetre):
        fenetre.blit(image_tuyau_haut, (self.x, self.hauteur - image_tuyau_haut.get_height()))
        fenetre.blit(image_tuyau_bas, (self.x, self.hauteur + self.espace))
