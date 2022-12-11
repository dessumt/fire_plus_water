# огонь и вода
import pygame
from light import *

pygame.init()

WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Mask:
    def __init__(self, filename, scale):
        self.image = pygame.image.load(filename).convert_alpha()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.mask = pygame.mask.from_surface(self.image)


def put_light_source():
    pass

light_surf = pygame.image.load('light_mask.png').convert_alpha()
light_surf = pygame.transform.scale(light_surf, (WIDTH, HEIGHT))

screen.fill((0,0,0))
running = True
mask = Mask('map2.png', (WIDTH-325, HEIGHT-215))
surf = pygame.Surface((WIDTH, HEIGHT))
surf.set_colorkey((0,0,0))

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    pos = pygame.mouse.get_pos()
    surf.fill((0,0,0,255))
    surf.set_alpha(200)
    pos_in_mask = pos[0] - mask.rect.x, pos[1] - mask.rect.y
    touching = mask.rect.collidepoint(*pos) and mask.mask.get_at(pos_in_mask)
    # screen.fill(pygame.Color('red') if touching else pygame.Color('green'))
    screen.blit(mask.image, mask.rect)
    cast_all_lights(surf, pos, mask)
    surf.blit(light_surf, (pos[0]-WIDTH / 2, pos[1]-HEIGHT / 2))
    screen.blit(surf, (0,0))


    pygame.display.update()
