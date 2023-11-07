import random
import pygame
import sys
import notes
import constant

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
        self, note_type, staff_loc, x=constant.WIDTH - 20, offset_x=0, offset_y=-20
    ):
        """
        Assign an obstacle note based upon a note_type argument provided.
        This is done so we can randomly generate obstacles later on in the game
        """
        self.note_type = note_type
        self.staff_loc = staff_loc
        image = "assets/images/"
        if note_type == 0:
            image += "whole-note.jpeg"
            offset_y = 0
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

        image = pygame.image.load(image)
        super().__init__(image, x, constant.STAFFPOS[staff_loc], offset_x, offset_y)

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

    RIGHT_LIMIT = constant.WIDTH / 2

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
        n_type = random.randint(0, 5)
        # randomly generate a staff location
        while True:
            s_loc = random.randint(0, 4)
            if self.rightmost_occupied_px[s_loc] == 0:
                break

        obstacle = Obstacle(note_type=n_type, staff_loc=s_loc)
        print("Adding obstacle at staff line", s_loc)
        self.obstacles.append(obstacle)
        self.rightmost_occupied_px[s_loc] = obstacle.x + obstacle.rect.width / 2

        return True

    def remove_obstacle(self, obstacle):
        """
        Remove an obstacle from the list
        """
        self.obstacles.remove(obstacle)

    def move_obstacles(self, surface):
        """
        Move all obstacles in the list, while updating the occupied staff lines
        """
        for obstacle in self.obstacles:
            obstacle.move_left(surface)
            w = obstacle.rect.width
            if obstacle.x + w / 2 < 0:
                self.remove_obstacle(obstacle)

        for i in range(0, 5):
            if self.rightmost_occupied_px[i] != 0:
                self.rightmost_occupied_px[i] -= 1
            if (
                self.rightmost_occupied_px[i] < self.RIGHT_LIMIT
                and self.rightmost_occupied_px[i] != 0
            ):
                self.rightmost_occupied_px[i] = 0
