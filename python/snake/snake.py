import pygame, sys, time, random

speed = 15

frame_size_x = 720
frame_size_y = 480

# Fix: The argument passed to set_mode should be a tuple of width and height
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# ...

while True:
    for event in pygame.event.get():  # Fix: pygame, not power
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Fix: sys.exit(), not sys.eexit()
        # ...

    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size

    # ...

    # Fix: Correct the spelling of "LEFT" in the elif condition
    elif event.key == pygame.K_LEFT or event.key == ord("a") and direction != "RIGHT":
        direction = "LEFT"
    elif event.key == pygame.K_RIGHT or event.key == ord("d") and direction != "LEFT":
        direction = "RIGHT"

    # ...

    # Fix: Correct the spelling of "LEFT" in the elif condition
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size

    # ...

    # Fix: Use pygame.draw.rect() instead of pygame.Rect()
    pygame.draw.rect(game_window, green, pygame.Rect(
        pos[0] + 2, pos[1] + 2, square_size - 2, square_size))

    # ...

    # Fix: Correct the spelling of "red" in the color definition
    pygame.draw.rect(game_window, red, pygame.Rect(
        food_pos[0], food_pos[1], square_size, square_size))

    # ...

    # Fix: Use random.randrange() instead of random.rangrange()
    food_pos = [
        random.randrange(1, frame_size_x // square_size) * square_size,
        random.randrange(1, frame_size_y // square_size) * square_size
    ]

    # ...
