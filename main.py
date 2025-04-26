import pygame
from constants import *
import player

def main ():
    pygame.init()
    Time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player = player.Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        Player.draw(screen)
        pygame.display.flip()
        
        dt = 1000/Time.tick(60)

if __name__=="__main__":
    main()