import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, COLORS, RUNNING
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.text_utils import TextUtils
import os

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 780
        self.y_pos_cloud = 180
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.text_utils = TextUtils()
        self.points = 0
        self.game_running = True
        self.death_count = 0
        self.powerup_manager = PowerUpManager()
        self.music_game = pygame.mixer.Sound(os.path.join('MUSICA/ferxxo.mp3'))
        self.music_game.set_volume(0.2)
        self.reset_button_rect = pygame.Rect(540, 290, 50, 30)
        
    

    def execute(self):
        self.music_game.play(-1)
        while self.game_running:
            if not self.playing:
                self.show_menu()
            # self.run()
    


    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.powerup_manager.reset_power_ups(self.points)
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self.points, self.game_speed, self.player)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_cloud()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

 
    def draw_cloud(self):    
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (self.x_pos_cloud + 250, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = SCREEN_WIDTH
        self.x_pos_cloud -= self.game_speed
    
    def score(self):
        self.points += 1
        text, text_rect = self.text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        self.game_running = True
        self.screen.fill(COLORS["white"])
        self.print_menu_elements()

        pygame.display.update()
        self.handle_key_event_on_menu()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        if self.death_count == 0:
            my_image = pygame.image.load("Portada/dino1.png")
            self.screen.blit(my_image, (20,150))
            text, text_rect = self.text_utils.get_centered_menssage("press any key to start")
            self.screen.blit(text, text_rect)

        elif self.death_count > 0:
            score, score_rect = self.text_utils.get_centered_menssage("Your Score: " + str(self.points), height = half_screen_height + 100)
            death, death_rect = self.text_utils.get_centered_menssage("Death count: " + str(self.death_count), height = half_screen_height + 150)

            self.screen.blit(score, score_rect)
            self.screen.blit(death, death_rect)
            my_image2 = pygame.image.load("Portada/GameOver.png")
            self.screen.blit(my_image2, (405, 385))
            my_image3 = pygame.image.load("Portada/Cara1.png")
            self.screen.blit(my_image3, (150, 150))
            my_image4 = pygame.image.load("Portada/Cara2.png")
            self.screen.blit(my_image4, (750, 150))
            reset_button = pygame.image.load("Portada/Reset.png")
            self.screen.blit(reset_button, (540, 290))
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0]:  # el botón izquierdo del ratón está presionado
                mouse_pos = pygame.mouse.get_pos()  # devuelve la posición actual del ratón
                if self.reset_button_rect.collidepoint(mouse_pos):  # si la posición del ratón está sobre el botón de reinicio
                    self.reset_game()


        self.screen.blit(RUNNING[0], (half_screen_width -20, half_screen_height -140))
        my_image = pygame.image.load("Portada/Lentes_ferxxo.png")
        self.screen.blit(my_image, (425, 70))

    
    
    def handle_key_event_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def reset_game(self):
        self.points = 0
        self.death_count =0
        self.music_game.stop()
        self.execute()
        
        
