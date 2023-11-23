import pygame
import sys
import globals

from pygame.locals import *


class Note(pygame.sprite.Sprite):
    """
    Class for a pygame sprite that will later serve as base class to Player, Obstacles and Powerups

    Attributes:
        image   : pygame.Surface object
        rect    : pygame.Rect object
        x       : int
        y       : int
    """

    def __init__(self, image, x, y, offset_x=0, offset_y=0, size_y=66):
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

        self.offset_y = offset_y
        # Resize image keeping the aspect ration intact
        self.image = pygame.transform.scale(
            self.image,
            (self.image.get_width() * (size_y / self.image.get_height()), size_y),
        )

        self.offset_x = offset_x + self.image.get_width() / 2

        self.rect = self.image.get_rect(center=(x + offset_x, y + offset_y))
        self.rect.center = (self.x + self.offset_x, self.y + self.offset_y)
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        self.orig_image = self.image.copy()

    def draw(self, surface):
        """
        Draw the Note object on the screen

        Args:
            surface: pygame.Surface object
        """
        surface.blit(self.image, self.rect)


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
        x=20,
        staff_loc=2,
        offset_x=0,
        offset_y=-22,
    ):
        """Set default position of the player class at third staff line in the beginning"""
        self.staff_loc = staff_loc
        super().__init__(image, x, globals.STAFFPOS[staff_loc], offset_x, offset_y)
        self.color_player()
        self.hit_count = 0
        self.score = 0
        self.prev_score = 0

    def color_player(self):
        colorImage = pygame.Surface(self.orig_image.get_size()).convert_alpha()
        colorImage.fill((100, 255, 100, 255))
        final_image = self.orig_image.copy()
        final_image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.image = final_image

    def convert_to_obstacle(self, surface, obstacle: Note):
        """
        Convert the player sprite to that of the obstacle
        """
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        self.image = obstacle.orig_image
        self.orig_image = self.image
        self.offset_x = obstacle.offset_x
        self.offset_y = obstacle.offset_y
        self.rect = self.image.get_rect(
            center=(self.x + self.offset_x, self.y + self.offset_y)
        )
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        self.color_player()
        self.draw(surface)

    def staff_movement(self, surface, dir: globals.Direction):
        """
        Move to the staff line above
        """
        if self.staff_loc == 0 and dir == globals.Direction.UP:
            return
        elif self.staff_loc == 4 and dir == globals.Direction.DOWN:
            return
        elif dir == None:
            return
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        prev_y = globals.STAFFPOS[self.staff_loc]
        self.staff_loc += dir.value
        new_y = globals.STAFFPOS[self.staff_loc]
        self.y = new_y
        self.rect.move_ip(0, new_y - prev_y)
        pygame.mixer.Sound.play(globals.STAFFSOUNDS[4 - self.staff_loc])
        self.draw(surface)
