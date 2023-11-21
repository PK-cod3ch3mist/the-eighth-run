import random
import pygame
import sys
import notes
import globals

from pygame.locals import *


class Powerup(notes.Note):
    """
    Powerup class for the game

    Attributes:
        powerup_type: int (Type of powerup for random generation)
        staff_loc   : int
        image       : pygame.Surface object
        rect        : pygame.Rect object
        x           : int
        y           : int

    Methods:
        color_powerup(): colors the powerup blue
        move_left()    : moves powerups across the screen
        hide()         : hides the powerup by drawing a black rectangle over it
    """

    def __init__(self, powerup_type, x=globals.WIDTH - 20, offset_x=0, offset_y=0):
        """
        Assign a powerup based upon a powerup_type argument provided.
        This is done so we can randomly generate powerups later on in the game
        """
        self.powerup_type = powerup_type
        image = "assets/images/"
        if powerup_type == 0:
            image += "whole-rest.png"
            offset_y = 7
            self.staff_loc = 1
        elif powerup_type == 1:
            image += "half-rest.png"
            offset_y = -7
            self.staff_loc = 2

        image = pygame.image.load(image)
        super().__init__(
            image, x, globals.STAFFPOS[self.staff_loc], offset_x, offset_y, height=15
        )
        self.color_powerup()

    def color_powerup(self):
        """
        Color the obstacle blue
        """
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill((100, 100, 255, 255))
        self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def move_left(self, surface, speed=1):
        """
        Move the powerup across the screen
        """
        # draw a black rect over the powerup's previous position
        pygame.draw.rect(surface, (0, 0, 0), self.rect)

        # move the powerup
        self.x -= speed
        self.rect.move_ip(-speed, 0)

        # draw the powerup in its new position
        self.draw(surface)

    def hide(self, surface):
        """
        Hide the powerup by drawing a black rectangle over it
        """
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
