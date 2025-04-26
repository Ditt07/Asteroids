import pygame
from constants import *

Time = pygame.time.Clock()
dt = 0

def main ():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = 1000/Time.tick(60)

if __name__=="__main__":
    main()