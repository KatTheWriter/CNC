import sys, pygame
pygame.init()

screen = pygame.display.set_mode((640,480))

background = pygame.image.load("bg.jpg")
backgroundRect = background.get_rect()

screen.blit(background, backgroundRect)
pygame.display.flip()

while 1:
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            print 'pressed UP'
        if pressed[pygame.K_DOWN]:
            print 'pressed DOWN'
        if pressed[pygame.K_LEFT]:
            print 'pressed LEFT'
        if pressed[pygame.K_RIGHT]:
            print 'pressed RIGHT'
        if pressed[pygame.K_q]:
            print 'pressed Q'
            pygame.display.quit()
            sys.exit()

