import pygame
from modules.ObjectManager import *
from modules.PlayerManager import *
from modules.BulletManager import *
from modules.EnemyManager import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((670, 670))
pygame.display.set_caption("test")

objects = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    keys = pygame.key.get_pressed()
    
    screen.fill('')

    fps = clock.get_fps()
    if not fps == 0:
        advanceStep(1/fps, objects)
        renderFrame(objects)
    clock.tick(60)
    

pygame.quit()