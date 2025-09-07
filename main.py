import sys
import pygame
from constants import *

# Load background tiles
bg_tiles = []
for i in range (1, 13):
    tile = pygame.image.load(f"/home/loren/chewie_the_chihuahua_2/assets/background/{i}.png")
    tile = pygame.transform.scale(tile, (BG_TILE_SIZE, BG_TILE_SIZE))
    bg_tiles.append(tile)

def create_background():
    """Create surface with tiled background"""
    # Set the tile arrangement
    grid_rows = 3
    grid_cols = 8

    # Set the scale to make tiles bigger
    bg_scale_factor = 4
    bg_scaled_tile_size = BG_TILE_SIZE * bg_scale_factor

    bg_width = grid_cols * bg_scaled_tile_size
    bg_height = grid_rows * bg_scaled_tile_size

    # Create a background surface
    background = pygame.Surface((bg_width, bg_height))

    # Fill with tiles in order
    for row in range(grid_rows):
        for col in range(grid_cols):
            row_start_tile = (row * 4) + 1
            tile_in_row = col % 4
            tile_number = row_start_tile + tile_in_row
            tile_index = tile_number - 1

            # Scale up tiles
            original_tile = bg_tiles[tile_index]
            scaled_tile = pygame.transform.scale(original_tile, (bg_scaled_tile_size, bg_scaled_tile_size))

            # Calculate position
            pos_x = col * bg_scaled_tile_size
            pos_y = row * bg_scaled_tile_size

            # Draw tiles
            background.blit(scaled_tile, (pos_x, pos_y))

    return background



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Call function to get background
    background_surface = create_background()

    bg_x = (SCREEN_WIDTH - background_surface.get_width()) // 2
    bg_y = (SCREEN_HEIGHT - background_surface.get_height()) // 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


        screen.blit(background_surface, (bg_x, bg_y))

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()