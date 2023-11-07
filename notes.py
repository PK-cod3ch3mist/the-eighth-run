import pygame
import sys
import constant

from pygame.locals import *


class Note:
    """
    Class for a pygame sprite that will later serve as base class to Player and Obstacles

    Attributes:
        image   : pygame.Surface object
        rect    : pygame.Rect object
        x       : int
        y       : int
    """

    def __init__(self, image, x, y, offset_x=0, offset_y=0):
        """
        Initialize a Note object

        Args:
            image: pygame.Surface object
            x    : int
            y    : int
        """
        self.image = image
        self.x = x
        self.y = y
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.rect = self.image.get_rect(center=(x + offset_x, y + offset_y))

    def draw(self, surface):
        """
        Draw the Note object on the screen

        Args:
            surface: pygame.Surface object
        """
        surface.blit(self.image, self.rect)


# [x]: Add a class for the player character which is inherited from Note class
# TODO: Add collision detection and player character convert feature
# TODO: Add music when the player scales up or down the staff lines
class Player(Note):
    """
    Player Class as a type of Note (attributes inherited)

    Attributes:
        staff_loc   : int (Current staff line on which located)

    Methods:
        staff_up()  : Go to the staff line above
        staff_down(): Go to the staff line below
    """

    def __init__(
        self,
        image=pygame.image.load("assets/images/eight-note.jpeg"),
        x=25,
        staff_loc=2,
        offset_x=0,
        offset_y=-20,
    ):
        """Set default position of the player class at third staff line in the beginning"""
        self.staff_loc = staff_loc
        super().__init__(image, x, constant.STAFFPOS[staff_loc], offset_x, offset_y)

    def staff_up(self):
        self.staff_loc -= 1

    def staff_down(self):
        self.staff_loc += 1
