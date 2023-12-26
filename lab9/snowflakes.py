import pygame
import sys
import random
import time

pygame.init()
clock = pygame.time.Clock()
width = 800
height = 800
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Snowy day')

snowflakes = []
lives = 5
score = 0
game_state = 'start'
difficulty = 'normal'

snowflake_image = pygame.image.load('snowflake.png')
snowflake_image = pygame.transform.scale(snowflake_image, (40, 40))
pygame.display.set_icon(snowflake_image)

class Snowflake:
    def __init__(self):
        self.x = random.randint(10, width - 10)
        self.y = 60
        self.velocity = random.uniform(1, 4) * difficulty_multiplier()
        self.remaining_horizontal_distance = 0

    def update(self):
        self.y += self.velocity

        if self.remaining_horizontal_distance == 0:
            self.remaining_horizontal_distance = random.randint(-20, 20)
        else:
            if self.remaining_horizontal_distance < 0:
                self.x -= 1
                self.remaining_horizontal_distance += 1
            elif self.remaining_horizontal_distance > 0:
                self.x += 1
                self.remaining_horizontal_distance -= 1

def difficulty_multiplier():
    if difficulty == 'easy':
        return 0.5
    elif difficulty == 'normal':
        return 1.0
    elif difficulty == 'hard':
        return 1.5

def update_snowflakes_velocity():
    for snowflake in snowflakes:
        snowflake.velocity = random.uniform(1, 4) * difficulty_multiplier()

def draw_text(text, position, size=40, color=(255, 255, 255)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def draw_text_center(text, height, size=40, color=(255, 255, 255)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(width / 2, height))
    screen.blit(text_surface, text_rect)


snowflakes = [Snowflake() for _ in range(int(width / 100))]
last_snowflake_addition = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "start":
                game_state = "playing"
            elif game_state == "playing":
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for snowflake in snowflakes:
                    if ( snowflake.x < mouse_x < snowflake.x + snowflake_image.get_width() and
                        snowflake.y < mouse_y < snowflake.y + snowflake_image.get_height()
                    ):
                        score += 1
                        snowflakes.remove(snowflake)

    screen.fill((12, 30, 81))

    if game_state == "start":
        draw_text_center("Start", height // 2 - 40)
        draw_text_center("Select difficulty:", height // 2)
        draw_text_center("e - easy, n - normal, h - hard", height // 2 + 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            difficulty = 'easy'
            update_snowflakes_velocity()
            game_state = "playing"
        elif keys[pygame.K_n]:
            difficulty = 'normal'
            update_snowflakes_velocity()
            game_state = "playing"
        elif keys[pygame.K_h]:
            difficulty = 'hard'
            update_snowflakes_velocity()
            game_state = "playing"

    elif game_state == "playing":
        for snowflake in snowflakes:
            screen.blit(snowflake_image, (int(snowflake.x), int(snowflake.y)))
            snowflake.update()

            if snowflake.x < 0 or snowflake.x > width:
                snowflakes.remove(snowflake)
            if snowflake.y >= height:
                snowflakes.remove(snowflake)
                lives -= 1

        draw_text(f"Score: {score}", (10, 10))
        draw_text(f"Lives: {lives}", (width - 120, 10))

        current_time = time.time()
        if current_time - last_snowflake_addition > 2:
            snowflakes.extend([Snowflake() for _ in range(5)])
            last_snowflake_addition = current_time

        if lives <= 0:
            game_state = "game over"

    elif game_state == "game over":
        draw_text_center("Game Over", height // 2 - 40)
        draw_text_center(f"Score: {score}", height // 2)
        draw_text_center("Click to restart", height // 2 + 40)

        if pygame.mouse.get_pressed()[0]:
            lives = 5
            score = 0
            snowflakes = []
            game_state = "start"

    pygame.display.flip()
    clock.tick(30)