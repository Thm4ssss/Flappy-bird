import pygame
from bird import Bird

class Game:
    def __init__(self,screen):
        self.screen=screen
        self.running=True
        self.bird=Bird()
        self.clock=pygame.time.Clock()
        self.bird=Bird()
    
    def handling_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
    
    def update(self):
        pass
    
    def display(self):
        pass
             
    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()


screen=pygame.display.set_mode((1080,720))
game=Game(screen)
game.run()