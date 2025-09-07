import sys
import pygame
import random
from constants import *

# Load background tiles
bg_tiles = []
for i in range (12):
    tile = pygame.load(f"\\wsl.localhost\\Ubuntu\\home\\loren\\chewie_the_chihuahua_2\\assets\\background\\{i}.png")
    tile = pygame.transform.scale(tile, (BG_TILE_SIZE, BG_TILE_SIZE))
    tiles.append(tile)

def create_background():
    """Create surface with tiled background"""
    # Calculate how many tiles we need
    tiles_x = SCREEN_WIDTH // BG_TILE_SIZE + 1
    tiles_y = SCREEN_HEIGHT // BG_TILE_SIZE + 1

    # Create background
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Fill with tiles
    



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()