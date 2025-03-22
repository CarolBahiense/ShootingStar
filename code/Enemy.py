import pygame

from Code.Const import ENTITY_SPEED, P_CENTER_H, WIN_HEIGHT
from Code.EnemyShoot import EnemyShoot
from Code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)



    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:
            self.health -=1