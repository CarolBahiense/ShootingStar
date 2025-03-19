#C
import pygame

C_WHITE = (255, 255, 255)
C_PURPLE = (31,12,81)
C_YELLOW = (252,222,28)
C_LIGHTBLUE = (0,186,255)

#E
ENTITY_SPEED = {'Level0':5,
                'Enemy': 3
                }
EVENT_ENEMY = pygame.USEREVENT + 1
#M
MENU_OPTION = ["HOW TO PLAY",
               "NEW GAME",
               "SCORE",
               "EXIT"
               ]
MUSIC_MENU = ('./asset/Menu.wav')
MUSIC_LEVEL = ('./asset/Level.flac')
MUSIC_SCORE = ('./asset/Score.wav')

#S
SPAWN_TIME = 1000
#W
WIN_WIDTH = 324
WIN_HEIGHT = 576

#POSITIONS HORIZONTAIS
P_CENTER_H = WIN_WIDTH / 2
P_LEFT_H = P_CENTER_H / 3
P_RIGHT_H = WIN_WIDTH - P_LEFT_H

#POSITIONS VERTICAIS
P_CENTER_V = WIN_HEIGHT / 2
P_UP_V = P_CENTER_V / 3
P_DOWN_V = WIN_WIDTH - P_UP_V

#POSITION MENU
P_MENU = P_CENTER_V+100