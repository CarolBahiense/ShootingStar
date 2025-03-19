import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.EntityFactory import EntityFactory
from code.Const import MUSIC_LEVEL, C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME
from code.Entity import Entity
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name:str):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY,SPAWN_TIME)

    def run(self, ):
        pygame.mixer_music.load(MUSIC_LEVEL)
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            ##Não está funcionando corretamente
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))

            #print texts
            self.level_text(20,f'fps:{clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(20, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

    def level_text(self, text_size : int, text : str, text_color: tuple, text_pos : tuple):
        text_font: Font = pygame.font.SysFont(name = "Lucinda Sans Typewriter", size= text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0],top = text_pos[1])
        self.window.blit(source=text_surf, dest= text_rect)