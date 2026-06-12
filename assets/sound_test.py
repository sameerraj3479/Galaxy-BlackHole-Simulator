import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("assets/space_ambience.wav")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

input("Sound chal rahi ho to Enter dabao...")