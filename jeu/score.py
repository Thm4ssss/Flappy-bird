import pygame

pygame.init()

#Chargement des images
restart_img = pygame.image.load('sprites/buttons/restart.png')
restart_hovered_img = pygame.image.load('sprites/buttons/restart_hovered.png')

# Options
font = pygame.font.SysFont('bauhaus93', 60)
white =(255,255,255)

def draw_text(text,font,text_color,x,y,screen):
    img = font.render(text,True,text_color)
    screen.blit(img,(x,y))
            
class Button():
    def __init__(self,x,y,image,image_hovered,screen):
        self.image = image
        self.image_hovered = image_hovered
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.screen = screen
    def draw(self):
        action = False
        
        # Récupère la position de la souris
        pos = pygame.mouse.get_pos()
        
        # Vérifie si la souris est sur le bouton
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        
        # Fait apparaître le bouton
        if action == True:
            self.screen.blit(self.image_hovered, (self.rect.x,self.rect.y))
        else:
            self.screen.blit(self.image, (self.rect.x,self.rect.y))
        
        return action