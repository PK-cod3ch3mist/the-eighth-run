import pygame
import sys
import globals

from pygame.locals import *


class Staff:
    """Class for different staff lines as platforms for the notes
    Attributes:
        rect: pygame.Rect object
        surf: pygame.Surface object
        y: int

    This will create a rectangular line accross the screen at a certain y value.
    """

    THICKNESS = 5

    def __init__(self, y):
        """
        Initialize a Staff object
        Args:
            y: int
        """
        self.surf = pygame.Surface((globals.WIDTH, self.THICKNESS))
        self.surf.fill((255, 255, 255))
        self.y = y
        self.rect = self.surf.get_rect(center=(globals.WIDTH / 2, self.y))

    def draw(self, surface):
        """
        Draw the Staff object on the screen
        Args:
            surface: pygame.Surface object
        """
        surface.blit(self.surf, self.rect)
