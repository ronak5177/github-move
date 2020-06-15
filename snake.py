import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
gray = (203, 220, 210)

screen_width = 900
screen_height = 600
# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake Game by Ronak Patel")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(gray)
        text_screen("Snake Game by Ronak Patel", black, screen_width/4, screen_height/3)
        text_screen("press space to play", black, screen_width/3, screen_height/3 + 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(40)

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def gameloop():
    # Initialize Game Specific Variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(50, screen_width / 2)
    food_y = random.randint(50, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 20
    fps = 40

    try:
        with open('high_score.txt', 'r') as f:
            highscore = f.read()
    except Exception as e:
        highscore = score
        print("File not Found")

    snake_list = []
    snake_length = 1
    # Game Loop


        # print("Game Over")
    while not exit_game:
        if game_over:

            with open('high_score.txt', 'w') as f:
                f.write(str(highscore))

            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, screen_width/4, screen_height/3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    # Adding Cheat Code
                    if event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 18 and abs(snake_y - food_y) < 18:
                score += 10
                food_x = random.randint(50, screen_width / 2)
                food_y = random.randint(50, screen_height / 2)
                snake_length += 5

                if score > int(highscore):
                    highscore = score

            gameWindow.fill(white)
            text_screen(f"Score : {score}  HighScore : {highscore}", red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            plot_snake(gameWindow, black, snake_list, snake_size)

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()



