import random
import time
import sys, pygame
pygame.init()
size = 1280, 720
window = pygame.display.set_mode(size)
screen = pygame.display.get_surface()
pygame.display.set_caption("Battle")
BLK = (0, 0, 0)

while True:
    clock = pygame.time.Clock()
    clock.tick(30)
    window.fill(BLK)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()