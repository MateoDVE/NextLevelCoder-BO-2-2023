import pygame
from dino_runner.utils.constants import FONT_STYLE2, COLORS, SCREEN_HEIGHT, SCREEN_WIDTH,FONT_STYLE

class TextUtils:
    def get_score_element(self, points):
        font = pygame.font.Font(FONT_STYLE2 ,22)
        text = font.render("Points" + str(points), True, COLORS["black"])
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        return text, text_rect
    
    def get_centered_menssage(self , message, width = SCREEN_WIDTH //2, height = SCREEN_HEIGHT //2 ):
        font = pygame.font.Font(FONT_STYLE ,40)
        text = font.render(message, True, COLORS["green"])
        text_rect = text.get_rect()
        text_rect.center = (width, height + 50) 
        return text, text_rect
    
    def get_time_element(self, time):
        font = pygame.font.Font(FONT_STYLE2, 22)
        text = font.render("Shield Time: " + str(time), True, COLORS["black"])
        text_rect = text.get_rect()
        text_rect.center = (250, 250)
        return text, text_rect

