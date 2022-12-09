# направление
import pygame
import math
v = (1, 1)
r = 5
EMBIANT_COLOR = (255, 247, 0, 230)
REFLECT_COLOR = (237, 204, 38, 220)

def find_light_collision(mask, v, mouse_pos, step, cat):
    if step == 0:
        return mouse_pos
    for i in range(5, 1000, step):
        cords = (mouse_pos[0] + v[0]*i, mouse_pos[1] + v[1]*i)
        pos_in_mask = cords[0] - cat.rect.x, cords[1] - cat.rect.y
        touching = cat.rect.collidepoint(*cords) and cat.mask.get_at(pos_in_mask)
        if touching:
            prev_cords = mouse_pos[0] + v[0]*(i-step), mouse_pos[1] + v[1]*(i-step)
            return find_light_collision(mask, v, prev_cords, step//2, cat)
    return mouse_pos[0] + v[0]*1000, mouse_pos[1] + v[1]*1000

def cast_light_line(Surface2draw, v, mask, mouse_pos, cat, step=10):
    cords = find_light_collision(mask, v, mouse_pos, step, cat)
    pygame.draw.line(Surface2draw, EMBIANT_COLOR, (mouse_pos[0], mouse_pos[1]), cords, 4)
    # pygame.draw.circle(Surface2draw, REFLECT_COLOR, cords, 6)

def cast_all_lights(Surface2draw, mask, mouse_pos, cat):
    for a in range(0, 36000,20):
        v = (math.sin(a/(2*math.pi/100)), math.cos(a/(2*math.pi/100)))
        cast_light_line(Surface2draw, v, mask, mouse_pos, cat)
