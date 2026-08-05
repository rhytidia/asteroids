import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # create new gui window
    clock = pygame.time.Clock() 
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # position player in middle
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #closing window ends the loop
                return
        updatable.update(dt)
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip() # refresh the screen
        dt = clock.tick(60) / 1000 # limit frame rate to 60 fps
       

if __name__ == "__main__":
    main()

''' dt and clock.tick():
dt = delta time: amount of time in secs since last frame rendered. 
clock.tick(60): loop runs at most 60 times/sec & returns how may ms since last call
dt = clock.tick(60) / 1000: turns ms into secs; dt is (approx) time between frames in seconds.

Then when objects move you can use x += SPEED * dt, and obj moves approx SPEED pixels per sec
over dt (time since the last frame refresh).

This means that even if some computers have faster frame rates than others the speed is similar
b/c you're moving by secs, not frames.'''