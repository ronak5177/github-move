import pygame

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0,0)
black = (0, 0, 0)

screen_width = 800
screen_height = 600
# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake Game by Ronak Patel")
pygame.display.update()

# Initialize Game Specific Variables

exit_game = False
game_over = False

# Game Loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True

    gameWindow.fill(white)
    pygame.display.update()

pygame.quit()
quit()
