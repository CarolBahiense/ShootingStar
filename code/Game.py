import sys

from Code.Const import WIN_WIDTH, MENU_OPTION
from Code.Const import WIN_HEIGHT
from Code.HowToPlay import HowToPlay
from Code.Menu import Menu
from Code.Level import Level
import pygame

from Code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self,):

        while True:
            htp = HowToPlay(self.window)
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return == MENU_OPTION[0]:
                htp.show()
            if menu_return == MENU_OPTION[1]:
                player_score = [0] #player 1
                level = Level(self.window, "Level", menu_return, player_score)
                level_return = level.run(player_score)
                if level_return == False:  # Se o jogador morreu, level_return será False
                    score.save(menu_return, player_score)
            elif menu_return == MENU_OPTION[2]:
                score.show()
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                sys.exit()  # Encerra o programa corretamente
            else:
                pass
