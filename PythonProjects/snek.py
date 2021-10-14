import pygame
import time
import random

# initalizes the screent
pygame.init()

# Sets color values
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

# Sets a caption on the window and size of window
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Snake game by Edureka")

# Creates values for size of block and speed of snake
snake_block = 10
snake_speed = 30

#intalize clock
clock = pygame.time.Clock()

#Sets a font
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

def gameLoop():
    # Sets inital game state
    game_over = False
    game_close = False

    # Initalize x and y values
    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while game_over != True:
        # Asks the user to play again 
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q to quit or C to play again", red)
            pygame.display.update()

            for even in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # If you quit the application the window will close
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
            # If key is pressed then...
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >=  dis_height or y1 < 0:
            game_over = True

        # Changes x and y based of key presses
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        # Creates player rectangle + food and then updates clock & display
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block] )
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()