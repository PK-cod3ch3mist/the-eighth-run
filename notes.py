import pygame
import sys
import globals

from pygame.locals import *


class Note(pygame.sprite.Sprite):
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
        super().__init__()
        self.image = image
        self.x = x
        self.y = y
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.rect = self.image.get_rect(center=(x + offset_x, y + offset_y))
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

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
        image=pygame.image.load("assets/images/eight-note.png"),
        x=40,
        staff_loc=2,
        offset_x=0,
        offset_y=-20,
    ):
        """Set default position of the player class at third staff line in the beginning"""
        self.staff_loc = staff_loc
        super().__init__(image, x, globals.STAFFPOS[staff_loc], offset_x, offset_y)
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill((134, 217, 119, 255))
        self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    # FIXME: Player chracter goes directly to last lines and then reports index out of range error
    def staff_up(self, surface):
        """
        Move to the staff line above
        """
        if self.staff_loc == 0:
            return
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        prev_y = globals.STAFFPOS[self.staff_loc]
        self.staff_loc -= 1
        new_y = globals.STAFFPOS[self.staff_loc]
        self.rect.move_ip(0, new_y - prev_y)
        pygame.mixer.Sound.play(globals.STAFFSOUNDS[4 - self.staff_loc])
        self.draw(surface)

    def staff_down(self, surface):
        """
        Move to the staff line below
        """
        if self.staff_loc == 4:
            return
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        prev_y = globals.STAFFPOS[self.staff_loc]
        self.staff_loc += 1
        new_y = globals.STAFFPOS[self.staff_loc]
        self.rect.move_ip(0, new_y - prev_y)
        pygame.mixer.Sound.play(globals.STAFFSOUNDS[4 - self.staff_loc])
        self.draw(surface)

    def check_collision(self):
        hits = pygame.sprite.spritecollide(
            self, globals.obstacles_group, False, collided=pygame.sprite.collide_mask
        )
        if hits:
            print("Collision detected: " + str(hits[0]))
            pygame.quit()
            sys.exit()
