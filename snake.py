# snake game

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set the window size
screen_size = (600, 600)

# Create the window
screen = pygame.display.set_mode(screen_size)

# Set the title of the window
pygame.display.set_caption("Snake")

# Set the dimensions of the snake
snake_block = 10

# Set the dimensions of the apple
apple_block = 10

# Set the initial position of the snake
snake_position = [100, 50]

# Initialize the snake body as a list of blocks
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set the initial position of the apple
apple_position = [random.randrange(1, (screen_size[0]//10)) * 10, random.randrange(1, (screen_size[1]//10)) * 10]
apple_spawn = True

# Set the initial direction of the snake
direction = 'RIGHT'
change_to = direction

# Set the score to 0
score = 0

# Set the speed of the game
speed = 15

# Define the colors
BLACK = pygame.Color(0, 0, 0)
GREEN = pygame.Color(0, 255, 0)
WHITE = pygame.Color(255, 255, 255)

# Function to display the score
def show_score(choice, color, font, size, x, y):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (x, y)
    else:
        score_rect.midtop = (x, y)
    screen.blit(score_surface, score_rect)

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 20)
    game_over_surface = my_font.render('Your Score is: ' + str(score), True, WHITE)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_size[0]/2, screen_size[1]/2)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake in the direction
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        score += 1
        apple_spawn = False
    else:
        snake_body.pop()
        
    if not apple_spawn:
        apple_position = [random.randrange(1, (screen_size[0]//10)) * 10, random.randrange(1, (screen_size[1]//10)) * 10]
    apple_spawn = True
    screen.fill(BLACK)
    
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], snake_block, snake_block))
        
    pygame.draw.rect(screen, WHITE, pygame.Rect(apple_position[0], apple_position[1], apple_block, apple_block))

    # Boundary conditions for snake
    if snake_position[0] > 600 or snake_position[0] < 0:
        game_over()
    if snake_position[1] > 600 or snake_position[1] < 0:
        game_over()
        
    # Self collision condition for snake
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    show_score(1, WHITE, 'times new roman', 20, screen_size[0]/2, 10)
    pygame.display.update()
    pygame.time.Clock().tick(speed)