import pygame
import sys

from pygame.locals import *

WIDTH = 800
HEIGHT = 450


class Note:
    """
    Class for a pygame sprite that will later serve as base class to Player and Obstacles
    Attributes:
        image: pygame.Surface object
        rect: pygame.Rect object
        x: int
        y: int
    """

    def __init__(self, image, x, y, offset_x=0, offset_y=0):
        """
        Initialize a Note object
        Args:
            image: pygame.Surface object
            x: int
            y: int
        """
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x + offset_x, y + offset_y))

    def draw(self, surface):
        """
        Draw the Note object on the screen
        Args:
            surface: pygame.Surface object
        """
        surface.blit(self.image, self.rect)
