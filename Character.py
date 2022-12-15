'''
character
'''
import pygame


class Character:
    def __init__(self, character_image=None):
        self.character_pos = [100, 550]
        self.character_image = character_image
        self.hitbox_size = 50
        self.is_touching = [False, False, False, False]
        self.vx = 0
        self.vy = 0
        self.isjump = False

    def move(self, motion):
        jumpcount = 0
        # по горизонтали
        if motion == 'LEFT' and self.character_pos[0]>55:
            # self.character_pos[0] -= 5
            self.vx = -5
        elif motion == 'RIGHT' and self.character_pos[0]<930:
            # self.character_pos[0] += 5
            self.vx = 5
        else:
            self.vx = 0
        self.character_pos[0] += self.vx

        # if not(isjump):
        #     if motion == 'UP':
        #         self.character_pos[1] -= 5
        #     elif motion == 'DOWN':
        #         self.character_pos[1] += 5
        #     elif motion == 'jump':
        #         isjump = True
        print(self.is_touching)
        if motion == 'UP' and self.is_touching[3]:
            # self.character_pos[1] += (jumpcount ** 2) / 3
            # self.character_pos[1] -= (jumpcount**2)/3
            self.vy = 5
            self.is_touching[3] = False
            # jumpcount -= 1
            # self.vy += jumpcount/3
        elif not self.is_touching[3]:
            jumpcount += 1
            self.vy -= jumpcount/3
        elif self.is_touching[3]:
            self.vy = 0

        self.character_pos[1] -= self.vy
        self.hitbox = pygame.Rect(self.character_pos[0], self.character_pos[1], self.hitbox_size, self.hitbox_size)

    def draw(self, surf, screen, color=(255,0,0,200)):
        pygame.draw.rect(surf, color, (self.character_pos[0]-self.hitbox_size/2, self.character_pos[1]-self.hitbox_size/2, self.hitbox_size, self.hitbox_size),8)
        screen.blit(surf, (0,0))

    def collision(self, mask):
        touching = False
        # self.phisical_hitbox_points = [[self.character_pos[0] - self.hitbox_size/2, self.character_pos[1] - self.hitbox_size/2],
        #                                [self.character_pos[0] - self.hitbox_size/2, self.character_pos[1]],
        #                                [self.character_pos[0] - self.hitbox_size/2, self.character_pos[1] + self.hitbox_size/2],
        #                                [self.character_pos[0], self.character_pos[1] - self.hitbox_size/2],
        #                                [self.character_pos[0], self.character_pos[1] + self.hitbox_size/2],
        #                                [self.character_pos[0] + self.hitbox_size/2, self.character_pos[1] - self.hitbox_size/2],
        #                                [self.character_pos[0] + self.hitbox_size/2, self.character_pos[1]],
        #                                [self.character_pos[0] + self.hitbox_size/2, self.character_pos[1] + self.hitbox_size/2]]
        self.phisical_hitbox_points = [[self.character_pos[0] - self.hitbox_size/2, self.character_pos[1]],
                                       [self.character_pos[0], self.character_pos[1] - self.hitbox_size/2],
                                       [self.character_pos[0], self.character_pos[1] + self.hitbox_size/2],
                                       [self.character_pos[0] + self.hitbox_size/2, self.character_pos[1]]]
        # pos_in_mask = self.character_pos[0] - mask.rect.x, self.character_pos[1] - mask.rect.y    
        for i, cords in enumerate(self.phisical_hitbox_points):
            pos_in_mask = cords[0] - mask.rect.x, cords[1] - mask.rect.y
            touching = mask.rect.collidepoint(*cords) and mask.mask.get_at(pos_in_mask)
            if touching == True:
                if i == 0:
                    # касание левой частью хитбокса
                    self.is_touching = [True, False, False, False]
                elif i == 3:
                    # касание правой частью
                    self.is_touching = [False, True, False, False]
                elif i == 1:
                    # касание верхней частью
                    self.is_touching = [False, False, True, False]
                elif i == 2:
                    # касание нижней
                    self.is_touching = [False, False, False, True]
                break
        if touching:
            if self.is_touching == [True, False, False, False]:
                self.vx = 0
            if self.is_touching == [False, True, False, False]:
                self.vx = 0
            if self.is_touching == [False, False, True, False]:
                self.vy = 0
            if self.is_touching == [False, False, False, True]:
                self.vy = 0
            color = (255, 255, 255)
        else:
            self.is_touching = [False, False, False, False]
            color = (255,0,0,200)
        return color

