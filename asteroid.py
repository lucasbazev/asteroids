import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        first_new_vector = self.velocity.rotate(angle)
        second_new_vector = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_new_asteroid = Asteroid(
            self.position.x, self.position.y, new_radius)
        second_new_asteroid = Asteroid(
            self.position.x, self.position.y, new_radius)

        first_new_asteroid.velocity = first_new_vector * 1.2
        second_new_asteroid.velocity = second_new_vector * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
