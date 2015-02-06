import sys, pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
background = pygame.image.load("background.bmp")
bod = pygame.image.load("bod3.png")
bodsize = 52
backgroundRect = background.get_rect()
pygame.display.flip()

x = 400
y = 300

def draw():
    moved = 0;
    screen.blit(background, backgroundRect)
    screen.blit(bod, (x,y))
    pygame.display.flip()

draw()

while 1:
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            print 'pressed UP'
            y = y - bodsize
            moved = 1
        if pressed[pygame.K_DOWN]:
            print 'pressed DOWN'
            y = y + bodsize
            moved = 1
        if pressed[pygame.K_LEFT]:
            print 'pressed LEFT'
        if pressed[pygame.K_RIGHT]:
            print 'pressed RIGHT'
        if pressed[pygame.K_q]:
            print 'pressed Q'
            pygame.display.quit()
            sys.exit()
        if moved:
            draw()

