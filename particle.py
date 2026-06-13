import pygame
import math
import random

class Particle:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.vx = random.uniform(-1.5, 1.5)
        self.vy = random.uniform(-1.5, 1.5)

        self.radius = random.randint(2, 4)

        self.color = random.choice([
            (255,255,255),
            (255,220,180),
            (180,220,255)
        ])

    def update(self, blackhole):

        dx = blackhole.x - self.x
        dy = blackhole.y - self.y

        distance = math.sqrt(dx * dx + dy * dy)

        if distance < blackhole.radius:
            blackhole.mass += 2
            return False

        force = blackhole.mass / (distance * distance)

        self.vx += force * dx / distance
        self.vy += force * dy / distance

        self.x += self.vx
        self.y += self.vy

        return True

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )