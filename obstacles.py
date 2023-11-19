import random
import pygame
import sys
import notes
import globals

from pygame.locals import *


class Obstacle(notes.Note):
    """
    Obstacle class as a type of Note

    Attributes:
        staff_loc   : int
        note_type   : int (Type of note for random generation)

    Methods:
        move_left() : moves obstacles across the screen
        hide()      : hides the obstacle by drawing a black rectangle over it
    """

    def __init__(
        self, note_type, staff_loc, x=globals.WIDTH - 20, offset_x=0, offset_y=-20
    ):
        """
        Assign an obstacle note based upon a note_type argument provided.
        This is done so we can randomly generate obstacles later on in the game
        """
        self.note_type = note_type
        self.staff_loc = staff_loc
        # FIXME: Change the offset x values so that all the notes align up properly on the left edge
        image = "assets/images/"
        if note_type == 0:
            image += "whole-note.png"
            offset_y = 0
        elif note_type == 1:
            image += "half-note.png"
        elif note_type == 2:
            image += "qtr-note.png"
        elif note_type == 3:
            image += "eight-note.png"
        elif note_type == 4:
            image += "eight-line.png"
            offset_x = 15
        elif note_type == 5:
            image += "sixteenth-notes.png"
            offset_x = 35

        image = pygame.image.load(image)
        super().__init__(image, x, globals.STAFFPOS[staff_loc], offset_x, offset_y)
        colorImage = pygame.Surface(self.orig_image.get_size()).convert_alpha()
        colorImage.fill((255, 100, 100, 255))
        self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def move_left(self, surface, speed=1):
        """
        Move the obstacle across the screen
        """
        # draw a black rect over the obstacle's previous position
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        # move the obstacle left by 1 pixel
        self.x -= speed
        self.rect.move_ip(-speed, 0)
        # draw the obstacle at its new position
        self.draw(surface)

    def hide(self, surface):
        """
        Hide the obstacle
        """
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
