import pygame

class BlackHole:

    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = 35

    def draw(self, screen):

        self.radius = int(35 + self.mass / 100)

        pygame.draw.circle(
            screen,
            (40, 0, 80),
            (int(self.x), int(self.y)),
            self.radius + 75
        )

        pygame.draw.circle(
            screen,
            (120, 0, 255),
            (int(self.x), int(self.y)),
            self.radius + 40
        )

        pygame.draw.circle(
            screen,
            (255, 120, 0),
            (int(self.x), int(self.y)),
            self.radius + 15,
            4
        )

        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (int(self.x), int(self.y)),
            self.radius
        )