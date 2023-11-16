# This file contains all the constant quantities used in the program
import pygame
import sys
from enum import Enum

from pygame.locals import *

WIDTH = 1000
HEIGHT = 450
STAFFPOS = (75, 150, 225, 300, 375)
FPS = 60

# Staff change sounds
pygame.mixer.init()
STAFFSOUNDS = (
    pygame.mixer.Sound("assets/sounds/E3.wav"),
    pygame.mixer.Sound("assets/sounds/G3.wav"),
    pygame.mixer.Sound("assets/sounds/B3.wav"),
    pygame.mixer.Sound("assets/sounds/D4.wav"),
    pygame.mixer.Sound("assets/sounds/F4.wav"),
)

TOTAL_STAFFS = len(STAFFSOUNDS)
TOTAL_NOTES = 6


class Direction(Enum):
    UP = -1
    DOWN = 1


obstacles_group = pygame.sprite.Group()
