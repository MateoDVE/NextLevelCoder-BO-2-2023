from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH
import random


class Bird(Obstacle):
    def __init__(self, image_list):
        self.type = 0
        super().__init__(image_list[self.type])
        self.rect.y = 250
        self.step_index = 0
    
    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.rect = self.image.get_rect()
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0
