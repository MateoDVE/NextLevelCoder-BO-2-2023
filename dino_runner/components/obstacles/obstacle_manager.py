from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.Bird import Bird
from dino_runner.components.obstacles.hasbulla import Hasbulla
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, HASBULLA
import pygame
import random

class ObstacleManager:

    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            rand = random.randint(0,2)
            if rand == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif rand == 1:
                self.obstacles.append(Bird(BIRD))
            elif rand == 2:
                self.obstacles.append(Hasbulla(HASBULLA))
                
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
            

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []
