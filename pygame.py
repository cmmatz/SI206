mport sys, pygame
pygame.init()

size = width, height = 600, 600
white = (255,255,255)
black = (0,0,0)


screen = pygame.display.set_mode(size)


Ex = pygame.image.load("Ex.png")
Oh = pygame.image.load("Oh.png")

def moveX(x,y):
    screen.blit(Ex, (x,y))

def moveO(x,y):
	screen.blit(Oh, (x,y))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(white)
    # pygame.display.flip()
    pygame.draw.lines(screen, black, True, [(200, 0), (200, 600)], 1)
    pygame.draw.lines(screen, black, True, [(400, 0), (400, 600)], 1)
    pygame.draw.lines(screen, black, True, [(0, 200), (600, 200)], 1)
    pygame.draw.lines(screen, black, True, [(0, 400), (600, 400)], 1)
    moveX(400,400)
    moveO(200,400)
    pygame.display.update()