import copy
import random
import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)

screen =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Huutista")
timer = pygame.time.Clock()

run = True

def draw_game(action):
    button_list = []

    if not action:
        
        pass

while run:
    timer.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.flip()
pygame.quit()    
