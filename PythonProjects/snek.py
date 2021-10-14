import pygame

def game():
    # initalizes the screent
    pygame.init()

    # Sets color values
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)

    # Sets a caption on the window and size of window
    dis = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Snake game by Edureka")

    game_over = False

    # Initalize x and y values
    x1 = 300
    y1 = 300

    x1_change = 0
    y1_change = 0

    #intalize clock
    clock = pygame.time.Clock()

    while game_over != True:
        # If you quit the application the window will close
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
            # If key is pressed then...
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

        # Changes x and y based of key presses
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        # Creates player rectangle and then updates clock & display
        pygame.draw.rect(dis, black, [x1, y1, 10, 10])

        pygame.display.update()

        clock.tick(30)

    pygame.quit()
    quit()

game()