import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]: # this creates a triangle for the player's ship
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None: # draw the triangle on the screen
        points_list = self.triangle()
        pygame.draw.polygon(screen, "cyan", points_list, LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    '''For rotate: if you do just rotate(dt) it will rotate clockwise (default).
    But if you use rotate(-dt) it's like rotation -= SPEED * dt. This
    means decreasing rotation, so counter-clockwise. move(-dt) similarly
    moves backwards bc default is forwards.'''

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def move(self, dt: float) -> None:
        # start with unit vector pointed straight down
        unit_vector = pygame.Vector2(0, 1)
        # rotate it so pointing in same direction as player
        rotated_vector = unit_vector.rotate(self.rotation)
        # make the vector the length the player should travel in the frame
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        # add the vector to the player's position to move them
        self.position += rotated_with_speed_vector