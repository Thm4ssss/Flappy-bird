from score import Button, draw_text
import pygame

class Restart_menu:
    def __init__(self,screen):
        self.screen=screen
        self.screen_width=self.screen.get_width()
        self.screen_height=self.screen.get_height()
        self.restart_button=Button(((self.screen_width)/2)+10,((self.screen_height)/2)+50,pygame.image.load("sprites/buttons/restart.png"),pygame.image.load("sprites/buttons/restart_hovered.png"),self.screen)
        self.quit_button=Button(((self.screen_width)/2)-10-120,((self.screen_height)/2)+50,pygame.image.load("sprites/buttons/quit.png"),pygame.image.load("sprites/buttons/quit_clicked.png"),self.screen)
    
    #on affiche les différents élements du menu 
    def display_restart_menu(self):
        draw_text("GAME OVER",pygame.font.SysFont('bauhaus93', 60),(255,240,240),(self.screen_width/2)-40,(self.screen_height/2)-50,self.screen)
        self.restart_button.draw()
        self.quit_button.draw()
    
    
fenetre=pygame.display.set_mode((900,520))
restart_menu=Restart_menu(fenetre)
running=True
while running:
    for event in pygame.event.get():
        if event==pygame.QUIT:
            running=False
    pygame.time.Clock().tick(60)
    restart_menu.display_restart_menu()
    pygame.display.flip()
pygame.quit()
    
        