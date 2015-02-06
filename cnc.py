import sys, pygame
pygame.init()

screen = pygame.display.set_mode((640,480))

background = pygame.image.load("balloons.jpg")
backgroundRect = background.get_rect()

screen.blit(background, backgroundRect)
pygame.display.flip()

while 1:
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        pygame.display.quit()
        sys.exit()

