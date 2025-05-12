import pygame
from constants import *
import player 
import asteroid
import asteroidfield
import sys
import bullet

def main ():
    pygame.init()
    Time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    asteroidfield.AsteroidField.containers = updatable
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    bullet.Bullet.containers=(drawable,updatable,bullets)


    Player = player.Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroid_field = asteroidfield.AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for astro in asteroids:
            if astro.colide(Player):
                print("Game over!")
                sys.exit()
            for shell in bullets:
                if astro.colide(shell):
                    shell.kill()
                    astro.split()

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        dt = Time.tick(60)/1000

if __name__=="__main__":
    main()