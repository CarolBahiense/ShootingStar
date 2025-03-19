import pygame.key

from code.Const import WIN_WIDTH, P_LEFT_H, P_RIGHT_H, P_CENTER_H
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.rect.centerx = P_CENTER_H

    def move(self):

        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    if self.rect.centerx == P_CENTER_H:
                        self.rect.centerx = P_LEFT_H
                    else:
                        self.rect.centerx = P_CENTER_H
                if events.key == pygame.K_RIGHT:
                    if self.rect.centerx == P_CENTER_H:
                        self.rect.centerx = P_RIGHT_H
                    else:
                        self.rect.centerx = P_CENTER_H
