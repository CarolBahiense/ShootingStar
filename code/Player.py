import pygame.key
from pygame import KEYDOWN, K_LEFT, K_RIGHT

from Code.Const import  P_CENTER_H, P_LEFT_H, P_RIGHT_H
from Code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.rect.centerx = P_CENTER_H

    def move(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if self.rect.centerx == P_RIGHT_H:
                    self.rect.centerx = P_CENTER_H
                elif self.rect.centerx == P_CENTER_H:
                    self.rect.centerx = P_LEFT_H

            elif event.key == K_RIGHT:
                if self.rect.centerx == P_LEFT_H:
                    self.rect.centerx = P_CENTER_H
                elif self.rect.centerx == P_CENTER_H:
                    self.rect.centerx = P_RIGHT_H



