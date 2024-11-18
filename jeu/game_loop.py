import pygame
from bird import Bird

class Game:
    def __init__(self,screen):
        self.screen=screen
        self.running=True
        self.bird=Bird()
        self.clock=pygame.time.Clock()
        self.bird=Bird()
        self.background=pygame.image.load("sprites/fond.png").convert()
        
    def handling_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
    
    def update(self):
        pass
    
    def display(self):
        self.screen.blit(self.background,(0,0))
        pygame.display.flip() 
           
    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()


screen=pygame.display.set_mode((950,520))
game=Game(screen)
game.run()