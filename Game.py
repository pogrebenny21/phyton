import random
import pygame

WIDTH = 600
HEIGHT = 600

clock = pygame.time.Clock()
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH , HEIGHT))

bg = pygame.image.load("back.jpg")
bg= pygame.transform.scale(bg, size: (1200, HEIGHT))
ground = pygame.image.load('ground.png')
ground = pygame.transform.scale(ground, size:(WIDTH + 200, 100))

flying = Falsese
game_over = False

pipe_grab = 200
pipe_frequence = 1500

last_pipe = pygame.time.get_triks() - pipe_frequence