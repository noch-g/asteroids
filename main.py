import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game Over!")
                exit()

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()