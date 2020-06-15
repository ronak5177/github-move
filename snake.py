import pygame

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0,0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600
# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake Game by Ronak Patel")
pygame.display.update()

# Initialize Game Specific Variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10


# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()



pygame.quit()
quit()
