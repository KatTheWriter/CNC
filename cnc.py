import sys, pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
background = pygame.image.load("background.bmp")
bod = pygame.image.load("bod3.png")
pygame.key.set_repeat(2,2)
bodsize = 52
backgroundRect = background.get_rect()
pygame.display.flip()

x = 400
y = 300
barheight = 125
step = 5

def draw():
    moved = 0;
    screen.blit(background, backgroundRect)
    screen.blit(bod, (x,y))
    pygame.display.flip()

def tell():
    print 'Bod is at (' + repr(x) + ',' + repr(y) + ')'

draw()

while 1:
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        tell()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            print 'pressed UP'
            if (y > 0 + step):
                y = y - step
                moved = 1
        if pressed[pygame.K_DOWN]:
            print 'pressed DOWN'
            if (y < 600-barheight-step):
               y = y + step
               moved = 1
        if pressed[pygame.K_LEFT]:
            print 'pressed LEFT'
            if (x > 0 + step):
                x = x - step
                moved = 1
        if pressed[pygame.K_RIGHT]:
            print 'pressed RIGHT'
            if (x < 800-52-step):
                x = x + step
                moved = 1
        if pressed[pygame.K_q]:
            print 'pressed Q'
            pygame.display.quit()
            sys.exit()
        if moved:
            draw()

