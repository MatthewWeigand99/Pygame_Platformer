import sys
import pygame

class Game:
    def __init__(self):  
        pygame.init()

        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        pygame.display.set_caption('Ninja Platformer')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(60) # 60 FPS loop
            
Game().run()