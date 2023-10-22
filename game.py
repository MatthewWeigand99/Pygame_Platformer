import sys
import pygame

from scripts.entities import PhysicsEntity

class Game:
    def __init__(self):  
        pygame.init()

        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        pygame.display.set_caption('Ninja Platformer')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        
    def run(self):
        while True:
            self.screen.fill((14, 219, 248)) # Background color
            
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_s or event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_s or event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60) # 60 FPS loop
            
Game().run()