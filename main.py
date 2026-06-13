import pygame
import random
import math

from blackhole import BlackHole
from particle import Particle

pygame.init()
pygame.mixer.init()

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Black Hole Simulator")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 24)

# Background Sound
try:
    pygame.mixer.music.load("assets/space_ambience.wav.mp3")
    pygame.mixer.music.play(-1)
except:
    print("Sound file not found")

blackhole = BlackHole(
    WIDTH // 2,
    HEIGHT // 2,
    1200
)

absorbed_count = 0

particles = []
background_stars = []

# Background stars
for i in range(1000):

    background_stars.append(
        (
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT),
            random.randint(100, 255)
        )
    )

# Galaxy particles
for i in range(400):

    angle = random.uniform(0, math.pi * 2)
    radius = random.randint(100, 450)

    x = WIDTH // 2 + radius * math.cos(angle)
    y = HEIGHT // 2 + radius * math.sin(angle)

    particles.append(
        Particle(x, y)
    )

running = True

while running:
    # Automatic Moving Black Hole
    blackhole.x = WIDTH // 2 + 300 * math.cos(
        pygame.time.get_ticks() / 1800
    )

    blackhole.y = HEIGHT // 2 + 220 * math.sin(
        pygame.time.get_ticks() / 1800
    )

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mx, my = pygame.mouse.get_pos()

            particles.append(
                Particle(mx, my)
            )

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                for i in range(100):

                    particles.append(
                        Particle(
                            random.randint(0, WIDTH),
                            random.randint(0, HEIGHT)
                        )
                    )

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        blackhole.mass += 10

    if keys[pygame.K_DOWN]:
        blackhole.mass -= 10

    screen.fill((5, 5, 20))

    # Background stars
    for x, y, brightness in background_stars:

        pygame.draw.circle(
            screen,
            (brightness, brightness, brightness),
            (x, y),
            1
        )

    blackhole.draw(screen)

    alive_particles = []

    for particle in particles:

        if particle.update(blackhole):

            particle.draw(screen)
            alive_particles.append(particle)

        else:

            absorbed_count += 1

    particles = alive_particles

    fps_text = font.render(
        f"FPS: {int(clock.get_fps())}",
        True,
        (255,255,255)
    )

    mass_text = font.render(
        f"Mass: {blackhole.mass}",
        True,
        (255,255,255)
    )

    star_text = font.render(
        f"Stars: {len(particles)}",
        True,
        (255,255,255)
    )

    absorbed_text = font.render(
        f"Absorbed: {absorbed_count}",
        True,
        (255,255,255)
    )

    screen.blit(fps_text, (10,10))
    screen.blit(mass_text, (10,40))
    screen.blit(star_text, (10,70))
    screen.blit(absorbed_text, (10,100))

    pygame.display.update()

pygame.quit()