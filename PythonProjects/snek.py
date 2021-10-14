import pygame

def game():
    # initalizes the screen and the size of it
    pygame.init()
    dis = pygame.display.set_mode((400,300))

    # Sets a caption on the window
    pygame.display.set_caption("Snake game by Edureka")

    # Initalizes color values using rgb values
    blue = (0,0,255)
    red = (255,0,0)

    game_over = False
    while game_over != True:
        # If you quit the application the window will close
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
        pygame.draw.rect(dis,blue,[200,150,10,10])
        pygame.display.update()
    pygame.quit()
    quit()

game()