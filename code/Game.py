import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self,):

        menu = Menu(self.window)
        menu_return = menu.run()


        if menu_return == MENU_OPTION[0]:
            level = Level(self.window, "Level")
            # howtoplay.run()
        elif menu_return == MENU_OPTION[1]:
            level = Level(self.window, "Level")
            level.run()
        elif menu_return == MENU_OPTION[2]:
            #score.show()
            level = Level(self.window, "Level")
        elif menu_return == MENU_OPTION[2]:
            pygame.quit()  # fechar a janela
            quit()  # terminar o pygame
        else:
            pass