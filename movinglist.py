import random
import pygame
import sys
import notes
import globals
from obstacles import Obstacle
from powerups import Powerup

from pygame.locals import *


class MovingList:
    """
    Class for a list of moving objects (obstacles or powerups)

    Attributes:
        obj_list   : list of Obstacle/Powerup objects
        rightmost_occupied_px: list of int (rightmost pixel occupied by an obstacle on each staff line)

    Methods:
        add_obstacle()  : adds an obstacle to the list
        add_powerup()   : adds a powerup to the list
        remove_object(): removes an obstacle/powerup from the list
        move_objects() : moves all objects in the list
    """

    RIGHT_LIMIT = globals.WIDTH - globals.blank_space

    def __init__(self):
        """
        Initialize an empty list of moving objects
        """
        self.obj_list = []
        self.rightmost_occupied_px = [0, 0, 0, 0, 0]
        self.speed = globals.START_SPEED

    def add_obstacle(self):
        """
        Add an obstacle to the list to an empty position on the staff
        """
        # Out of all unoccupied staff lines, randomly choose one.
        # If any 4 or all are occupied, return False
        unoccupied_cnt = self.rightmost_occupied_px.count(0)
        if unoccupied_cnt == 0 or unoccupied_cnt == 1:
            return False

        unoccupied = [i for i, x in enumerate(self.rightmost_occupied_px) if x == 0]
        s_loc = random.choice(unoccupied)

        # randomly generate a number
        n_type = random.randint(0, globals.TOTAL_NOTES - 1)

        obstacle = Obstacle(note_type=n_type, staff_loc=s_loc)
        # print("Adding obstacle at staff line", s_loc)
        self.obj_list.append(obstacle)
        globals.moving_group.add(obstacle)
        self.rightmost_occupied_px[s_loc] = obstacle.x + obstacle.rect.width / 2

        return True

    def add_powerup(self):
        """
        Add a powerup to the list to an empty position on the staff
        """
        # Out of staff lines 1 and 2, randomly choose one which is not occupied.
        # If both are occupied, return False
        if self.rightmost_occupied_px[1] == 0 and self.rightmost_occupied_px[2] == 0:
            s_loc = random.randint(1, 2)
        elif self.rightmost_occupied_px[1] == 0:
            s_loc = 1
        elif self.rightmost_occupied_px[2] == 0:
            s_loc = 2
        else:
            return False

        n_type = s_loc - 1
        powerup = Powerup(powerup_type=n_type)
        # print("Adding obstacle at staff line", s_loc)
        self.obj_list.append(powerup)
        globals.moving_group.add(powerup)
        self.rightmost_occupied_px[s_loc] = powerup.x + powerup.rect.width / 2

        return True

    def remove_object(self, moving_object):
        """
        Remove the moving object from the list
        """
        self.obj_list.remove(moving_object)
        globals.moving_group.remove(moving_object)

    def move_objects(self, surface):
        """
        Move all objects in the list, while updating the occupied staff lines
        """
        for moving_object in self.obj_list:
            moving_object.move_left(surface, self.speed)
            w = moving_object.rect.width
            if moving_object.x + moving_object.offset_x + w / 2 < 0:
                self.remove_object(moving_object)

        for i in range(0, 5):
            if self.rightmost_occupied_px[i] != 0:
                self.rightmost_occupied_px[i] -= self.speed
            if (
                self.rightmost_occupied_px[i] < self.RIGHT_LIMIT
                and self.rightmost_occupied_px[i] != 0
            ):
                self.rightmost_occupied_px[i] = 0
