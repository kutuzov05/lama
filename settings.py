import pygame


pygame.init()
width, height = 750, 750
screen = pygame.display.set_mode((width, height))
FPS = 60
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (215, 235, 255)
RED = (255, 215, 215)

words = ["Wasser", "Feuer", "Erde", "Luft"]
slot_l, slot_r = None, None
pos = 0
scroll_strength = height*0.03
