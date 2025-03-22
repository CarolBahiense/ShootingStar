import random
import sys

import pygame.display
from pygame import Surface, Rect, K_ESCAPE
from pygame.font import Font

from Code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, MUSIC_LEVEL, C_LIGHTBLUE, P_CENTER_H, \
    P_CENTER_V
from Code.Enemy import Enemy
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory
from Code.EntityMediator import EntityMediator
from Code.Player import Player


class Level:
    def __init__(self, window: Surface, name:str, game_mode:str,player_score:list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode #Modo de jogo
        self.entity_list: list[Entity]=[]
        self.entity_list.extend(EntityFactory.get_entity(self.name))
        player = EntityFactory.get_entity('Player')
        player.score = player_score[0]
        self.player = player
        self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Configura o timer para spawn de inimigos

    def run(self,player_score:list[int]):
        pygame.mixer_music.load(MUSIC_LEVEL)
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)

                if ent.name !='Player':
                    ent.move()
                if ent.name == 'Player':
                    ent.score+=1
                    self.level_text(20, f'Health:{ent.health} | Score: {ent.score}', C_LIGHTBLUE, (10, 10))
            for event in pygame.event.get():
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.player.move(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True
            if not found_player:
                player_score[0] = self.player.score  # Salvar a pontuação antes de ir para a tela de score
                return False

            #print texts

            pygame.display.flip()

            ##Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)



    def level_text(self, text_size : int, text : str, text_color: tuple, text_pos : tuple):
        text_font: Font = pygame.font.SysFont(name = "Lucinda Sans Typewriter", size= text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0],top = text_pos[1])
        self.window.blit(source=text_surf, dest= text_rect)