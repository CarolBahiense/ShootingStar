import pygame
from pygame.examples.grid import WINDOW_WIDTH

#c
C_WHITE = (255, 255, 255)
C_YELLOW = (252,222,28)
C_LIGHTBLUE = (0,186,255)


#e
ENTITY_SPEED = {
    'Level0' : 6,
    'Player': 0,
    'Enemy' : 4,
}
ENTITY_HEALTH = {
    'Level0' : 999,
    'Player' : 3,
    'Enemy' : 1,
}
ENTITY_DAMAGE = {
    'Level0' : 0,
    'Player' : 1,
    'Enemy' : 1,

}
ENTITY_SCORE = {
    'Level0' : 0,
    'Player' : 0,
    'Enemy' : 0,

}

EVENT_ENEMY = pygame.USEREVENT + 1

#m
MENU_OPTION =('HOW TO PLAY',
              'NEW GAME',
              'SCORE',
              'EXIT')

MUSIC_MENU = ('./asset/Menu.wav')
MUSIC_LEVEL = ('./asset/Level.flac')
MUSIC_SCORE = ('./asset/Score.wav')

#s
SPAWN_TIME = 800


#t
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

#w
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

#s
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 210),
    'EnterName': (WIN_WIDTH / 2, 240),
    'Label' : (WIN_WIDTH/2,P_CENTER_V-(20*1)),
    'Name' : (WIN_WIDTH/2,260),
    0: (WIN_WIDTH/2 , P_CENTER_V),
    1: (WIN_WIDTH/2 , P_CENTER_V+(20*1)),
    2: (WIN_WIDTH/2 , P_CENTER_V+(20*2)),
    3: (WIN_WIDTH/2 , P_CENTER_V+(20*3)),
    4: (WIN_WIDTH/2 , P_CENTER_V+(20*4)),
    5: (WIN_WIDTH/2 , P_CENTER_V+(20*5)),
    6: (WIN_WIDTH/2 , P_CENTER_V+(20*6)),
    7: (WIN_WIDTH/2 , P_CENTER_V+(20*7)),
    8: (WIN_WIDTH/2 , P_CENTER_V+(20*8)),
    9: (WIN_WIDTH /2, P_CENTER_V+(20*9)),
}

HTP_TEXTS = (
    '¬Use LEFT arrow to move left' ,
    '¬Use RIGHT arrow to move right',
    '¬Press ESC to go back to Main Menu',
    '¬Earn points by surviving',
    'as long as possible.',
    '¬Avoid the stars! If you',
    'hit one, you lose a life.',
    '¬You have 3 lives, when you',
    'lose them all, the game is over.',
    '¬The longer you survive, the',
    'higher your score.',
    '¬Test your reflexes and see',
    'how long you can last!',
)
HTP_POS ={
    'Title': (WIN_WIDTH/2 , 70),
    'Subtitle' : (WIN_WIDTH/2 , 110),
    'Control1': (WIN_WIDTH/2 , 130),
    'Control2': (WIN_WIDTH/2 , 150),
    'Control3': (WIN_WIDTH/2 , 170),
    'Subtitle2': (WIN_WIDTH / 2, 210),
    'Primeiro': (WIN_WIDTH/2 , 230),
    'Segundo': (WIN_WIDTH/2 , 250),
    'Terceiro': (WIN_WIDTH/2 , 290),
    'Quarto': (WIN_WIDTH/2 , 310),
    'Quinto': (WIN_WIDTH / 2, 350),
    'Sexto' : (WIN_WIDTH / 2, 370),
    'Setimo' : (WIN_WIDTH / 2, 410),
    'Oitavo' : (WIN_WIDTH / 2, 430),
    'Nono' : (WIN_WIDTH / 2, 470),
    'Decimo' :(WIN_WIDTH / 2, 490),
    'Rodape' : (WIN_WIDTH / 2, 530)
}