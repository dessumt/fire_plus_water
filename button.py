'''
Button
'''
import pygame


BUTTON_FILES = ['button_casual.png', 'button_pressed.png']

class Button:
    def __init__(self, button_pos, mask, surface):
        self.surface = surface
        self.button_pos = button_pos[0] - mask.rect.x, button_pos[1] - mask.rect.y
        self.images = []
        self.images.append(pygame.image.load('button_casual.png').convert_alpha())
        self.images.append(pygame.image.load('button_pressed.png').convert_alpha())
        self.index = 0
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (40,10))
        self.button_hitbox = pygame.Rect(self.button_pos[0] + 15, self.button_pos[1] + 13, 30, 10)

    def is_button_pressed(self, character):
        '''
        character has: rect(hitbox), pos(of centre hitbox)
        '''
        character_hitbox = character.hitbox
        touching = pygame.Rect.colliderect(character_hitbox, self.button_hitbox)
        # print(touching)
        if touching:
            self.draw(self.images[1], (self.button_pos[0]-15, self.button_pos[1]-15))
        else:
            self.draw(self.images[0], (self.button_pos[0]-15, self.button_pos[1]-15))
    def draw(self, image, pos):
        self.surface.blit(image, pos)


class Platform:
    def __init__(self, platform_pos, mask, surface):
        self.surface = surface
        self.platform_pos = platform_pos[0] - mask.rect.x, platform_pos[1] - mask.rect.y
        self.images = []
        self.images.append(pygame.image.load('platform_casual.png').convert_alpha())
        self.images.append(pygame.image.load('platform_bright.png').convert_alpha())
