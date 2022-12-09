# огонь и вода
import pygame
from light import *

pygame.init()

WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Cat:
    def __init__(self):
        self.image = pygame.image.load('mask.png').convert_alpha()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.scale(self.image, (WIDTH/2 - 100, HEIGHT / 2 - 100))
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.mask = pygame.mask.from_surface(self.image)

light_surf = pygame.image.load('light_mask.png').convert_alpha()
light_surf = pygame.transform.scale(light_surf, (WIDTH, HEIGHT))

screen.fill((0,0,0))
running = True
cat = Cat()
surf = pygame.Surface((WIDTH, HEIGHT))
surf.set_colorkey((0,0,0))

while running:
    screen.fill((0,0,0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    pos = pygame.mouse.get_pos()
    surf.fill((0,0,0,255))
    surf.set_alpha(200)
    pos_in_mask = pos[0] - cat.rect.x, pos[1] - cat.rect.y
    touching = cat.rect.collidepoint(*pos) and cat.mask.get_at(pos_in_mask)
    # screen.fill(pygame.Color('red') if touching else pygame.Color('green'))
    screen.blit(cat.image, cat.rect)
    cast_all_lights(surf, cat.mask, pos, cat)
    surf.blit(light_surf, (pos[0]-WIDTH / 2, pos[1]-HEIGHT / 2))
    screen.blit(surf, (0,0))


    pygame.display.update()