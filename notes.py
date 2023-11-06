import pygame
import sys

from pygame.locals import *

WIDTH = 800
HEIGHT = 450
STAFFPOS = (75, 150, 225, 300, 375)


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
        image="assets/images/eight-note.jpeg",
        x=20,
        staff_loc=2,
        offset_x=0,
        offset_y=-20,
    ):
        """Set default position of the player class at third staff line in the beginning"""
        self.staff_loc = staff_loc
        super().__init__(image, x, STAFFPOS[staff_loc], offset_x, offset_y)

    def staff_up(self):
        self.staff_loc -= 1

    def staff_down(self):
        self.staff_loc += 1


# [x]: Add class for obstacles which is inherited from Note class
# TODO: Add collision detection for obstacles
class Obstacle(Note):
    """
    Obstacle class as a type of Note

    Attributes:
        staff_loc   : int
        note_type   : int (Type of note for random generation)

    Methods:
        move_left() : moves obstacles across the screen
    """

    def __init__(self, note_type, x, staff_loc, offset_x=0, offset_y=-20):
        """
        Assign an obstacle note based upon a note_type argument provided.
        This is done so we can randomly generate obstacles later on in the game
        """
        self.note_type = note_type
        self.staff_loc = staff_loc
        image = "assets/images/"
        if note_type == 0:
            image += "whole-note.jpeg"
        elif note_type == 1:
            image += "half-note.jpeg"
        elif note_type == 2:
            image += "qtr-note.jpeg"
        elif note_type == 3:
            image += "eight-note.jpeg"
        elif note_type == 4:
            image += "eight-line.jpeg"
        elif note_type == 5:
            image += "sixteenth-notes.jpeg"
        super().__init__(image, x, STAFFPOS[staff_loc], offset_x, offset_y)

    def move_left(self):
        self.x -= 1
