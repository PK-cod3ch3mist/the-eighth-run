# This file contains all the constant quantities used in the program
import pygame
import sys
from enum import Enum

from pygame.locals import *

WIDTH = 1000
HEIGHT = 750
STAFFPOS = (175, 275, 375, 475, 575)
FPS = 60

obstacle_probability = 0.1
powerup_probability = 0.01
blank_space = 500

PROB_LEVEL = 30
PROB_INCREASE = 0.05

SPACE_LEVEL = 60
MIN_BLANK_SPACE = 300
SPACE_DECREASE = 5

START_SPEED = 2
SPEED_LEVEL = 15
SPEED_INCREASE = 1


# Staff change sounds
pygame.mixer.init()

STAFFSOUNDS = (
    pygame.mixer.Sound("assets/sounds/D#3.wav"),
    pygame.mixer.Sound("assets/sounds/G3.wav"),
    pygame.mixer.Sound("assets/sounds/A#3.wav"),
    pygame.mixer.Sound("assets/sounds/D4.wav"),
    pygame.mixer.Sound("assets/sounds/F4.wav"),
)
for sound in STAFFSOUNDS:
    sound.set_volume(0.25)

TOTAL_STAFFS = len(STAFFSOUNDS)
TOTAL_NOTES = 6
TOTAL_POWERUPS = 2


class Direction(Enum):
    UP = -1
    DOWN = 1


moving_group = pygame.sprite.Group()
