import pygame
import sys
import notes
import platforms
import constant

from pygame.locals import *

# Basic pygame boilerplate code with event loop
pygame.init()
DISPLAYSURF = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT))
pygame.display.set_caption("The Eighth Run")

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Display some of the notes.Note objects
    note1 = notes.Note(
        pygame.image.load("assets/images/whole-note.jpeg"),
        100,
        constant.STAFFPOS[0],
        0,
        1,
    )
    note2 = notes.Note(
        pygame.image.load("assets/images/half-note.jpeg"),
        200,
        constant.STAFFPOS[1],
        0,
        -20,
    )
    note3 = notes.Note(
        pygame.image.load("assets/images/qtr-note.jpeg"),
        300,
        constant.STAFFPOS[2],
        0,
        -20,
    )
    note1.draw(DISPLAYSURF)
    note2.draw(DISPLAYSURF)
    note3.draw(DISPLAYSURF)

    # Display the 5 staff lines at equal intervals in the y direction
    staff1 = platforms.Staff(constant.STAFFPOS[0])
    staff2 = platforms.Staff(constant.STAFFPOS[1])
    staff3 = platforms.Staff(constant.STAFFPOS[2])
    staff4 = platforms.Staff(constant.STAFFPOS[3])
    staff5 = platforms.Staff(constant.STAFFPOS[4])
    staff1.draw(DISPLAYSURF)
    staff2.draw(DISPLAYSURF)
    staff3.draw(DISPLAYSURF)
    staff4.draw(DISPLAYSURF)
    staff5.draw(DISPLAYSURF)
    pygame.display.update()
