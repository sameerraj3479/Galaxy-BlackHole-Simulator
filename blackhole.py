import pygame

class BlackHole:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = 35

    def draw(self, screen):

        # Outer glow
        pygame.draw.circle(
            screen,
            (40, 0, 80),
            (int(self.x), int(self.y)),
            110
        )

        # Purple glow
        pygame.draw.circle(
            screen,
            (120, 0, 255),
            (int(self.x), int(self.y)),
            80
        )

        # Accretion ring
        pygame.draw.circle(
            screen,
            (255, 120, 0),
            (int(self.x), int(self.y)),
            55,
            4
        )

        # Black hole center
        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (int(self.x), int(self.y)),
            self.radius
        )