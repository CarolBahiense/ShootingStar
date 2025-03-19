from code.Const import P_CENTER_H, ENTITY_SPEED, WIN_HEIGHT
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.rect.centerx = P_CENTER_H

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >=WIN_HEIGHT:
            self.rect.bottom = 0