import pygame
import sys
import notes
import platforms

from pygame.locals import *

# Basic pygame boilerplate code with event loop
pygame.init()
WIDTH = 800
HEIGHT = 450
STAFFPOS = (75, 150, 225, 300, 375)
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Eighth Run")

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Display some of the notes.Note objects
    note1 = notes.Note(
        pygame.image.load("assets/images/whole-note.jpeg"), 100, STAFFPOS[0], 0, 1
    )
    note2 = notes.Note(
        pygame.image.load("assets/images/half-note.jpeg"), 200, STAFFPOS[1], 0, -20
    )
    note3 = notes.Note(
        pygame.image.load("assets/images/qtr-note.jpeg"), 300, STAFFPOS[2], 0, -20
    )
    note1.draw(DISPLAYSURF)
    note2.draw(DISPLAYSURF)
    note3.draw(DISPLAYSURF)

    # Display the 5 staff lines at equal intervals in the y direction
    staff1 = platforms.Staff(STAFFPOS[0])
    staff2 = platforms.Staff(STAFFPOS[1])
    staff3 = platforms.Staff(STAFFPOS[2])
    staff4 = platforms.Staff(STAFFPOS[3])
    staff5 = platforms.Staff(STAFFPOS[4])
    staff1.draw(DISPLAYSURF)
    staff2.draw(DISPLAYSURF)
    staff3.draw(DISPLAYSURF)
    staff4.draw(DISPLAYSURF)
    staff5.draw(DISPLAYSURF)
    pygame.display.update()
