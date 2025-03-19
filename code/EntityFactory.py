import random

from code.Background import Background
from code.Const import WIN_HEIGHT, P_CENTER_H, WIN_WIDTH, P_LEFT_H, P_RIGHT_H
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(f'Level{i}', (0, 0)))
                    list_bg.append(Background(f'Level{i}', (0, (-WIN_HEIGHT))))
                return list_bg
            case 'Player':
                return Player('Player', (P_CENTER_H, WIN_HEIGHT - 130))
            case 'Enemy':
                values = [P_LEFT_H, P_CENTER_H, P_RIGHT_H]
                return Enemy('Enemy', (random.choice(values),0 - 30))
