from dino_runner.components.obstacles.obstacle import Obstacle
import random


class Hasbulla(Obstacle):
    def __init__(self, image_list):
        self.type = random.randint(0,1)
        super().__init__(image_list[self.type])
        self.rect.y = 300
        self.step_index = 0
    