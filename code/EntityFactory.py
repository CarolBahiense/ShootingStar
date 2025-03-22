import random

from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT, P_CENTER_H, P_LEFT_H, P_RIGHT_H
from Code.Player import Player
from Code.Enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name : str, position=(0,0)):
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
                return Enemy('Enemy', (random.choice([(P_LEFT_H, -10), (P_CENTER_H, -10), (P_RIGHT_H, -10)])))