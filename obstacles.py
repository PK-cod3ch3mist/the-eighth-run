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
        colorImage.fill((245, 123, 86, 255))
        self.image.blit(colorImage, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def move_left(self, surface):
        """
        Move the obstacle across the screen
        """
        # draw a black rect over the obstacle's previous position
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        # move the obstacle left by 1 pixel
        self.x -= 1
        self.rect.move_ip(-1, 0)
        # draw the obstacle at its new position
        self.draw(surface)

    def hide_obstacle(self, surface):
        """
        Hide the obstacle
        """
        pygame.draw.rect(surface, (0, 0, 0), self.rect)


class ObstacleList:
    """
    Class for a list of obstacles

    Attributes:
        obstacles   : list of Obstacle objects
        rightmost_occupied_px: list of int (rightmost pixel occupied by an obstacle on each staff line)

    Methods:
        add_obstacle()  : adds an obstacle to the list
        remove_obstacle(): removes an obstacle from the list
        move_obstacles() : moves all obstacles in the list
    """

    RIGHT_LIMIT = globals.WIDTH / 2

    def __init__(self):
        """
        Initialize an empty list of obstacles
        """
        self.obstacles = []
        self.rightmost_occupied_px = [0, 0, 0, 0, 0]

    def add_obstacle(self):
        """
        Add an obstacle to the list to an empty position on the staff
        """
        # if no staff line has righmost pixel as zero, that means all staff lines are occupied, so return False
        if all(x != 0 for x in self.rightmost_occupied_px):
            return False

        # randomly generate a number
        n_type = random.randint(0, globals.TOTAL_NOTES - 1)
        # randomly generate a staff location
        while True:
            s_loc = random.randint(0, globals.TOTAL_STAFFS - 1)
            if self.rightmost_occupied_px[s_loc] == 0:
                break

        obstacle = Obstacle(note_type=n_type, staff_loc=s_loc)
        # print("Adding obstacle at staff line", s_loc)
        self.obstacles.append(obstacle)
        globals.obstacles_group.add(obstacle)
        self.rightmost_occupied_px[s_loc] = obstacle.x + obstacle.rect.width / 2

        return True

    def remove_obstacle(self, obstacle):
        """
        Remove an obstacle from the list
        """
        self.obstacles.remove(obstacle)
        globals.obstacles_group.remove(obstacle)

    def move_obstacles(self, surface):
        """
        Move all obstacles in the list, while updating the occupied staff lines
        """
        for obstacle in self.obstacles:
            obstacle.move_left(surface)
            w = obstacle.rect.width
            if obstacle.x + obstacle.offset_x + w / 2 < 0:
                self.remove_obstacle(obstacle)

        for i in range(0, 5):
            if self.rightmost_occupied_px[i] != 0:
                self.rightmost_occupied_px[i] -= 1
            if (
                self.rightmost_occupied_px[i] < self.RIGHT_LIMIT
                and self.rightmost_occupied_px[i] != 0
            ):
                self.rightmost_occupied_px[i] = 0
