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
moved = 0

displaylist = [
        {
        "name": "shed",
        "obstacle": 1,
        "colour": 0xbbbbbb,
        "location": ( (565,0), (600,125) )
        }
    ]

def draw():
    global moved
    moved = 0;
    screen.blit(background, backgroundRect)
    for obj in displaylist:
        screen.fill(obj["colour"], obj["location"])
                            
    pygame.draw.line(screen, 0xffffff, (0,y), (800,y), 1)
    pygame.draw.line(screen, 0xffffff, (x,0), (x,600), 1)
    screen.blit(bod, (x,y))
    pygame.display.flip()

def tell():
    print 'Bod is at (' + repr(x) + ',' + repr(y) + ')'

def move(dx,dy):
    global x, y, moved
    nx = x + dx
    ny = y + dy
    # edges
    if (ny < 0 + step or ny > 600-barheight-step or nx < 0 + step or nx > 800-52-step):
        print 'No Way, Bod'
        return
    # shed
    if (ny < 125 and nx > 515):
        print 'Keep out of the shed, Bod'
        return

    x = nx
    y = ny
    moved = 1

def walkto(pos):
    global x, y, moved
    print 'Moving to (' + repr(pos[0]) + ',' + repr(pos[1]) + ')'
    x = pos[0]
    y = pos[1]
    moved = 1 

draw()

while 1:
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        tell()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            print 'pressed UP'
            move(0,-step)
        if pressed[pygame.K_DOWN]:
            print 'pressed DOWN'
            move(0,step)
        if pressed[pygame.K_LEFT]:
            print 'pressed LEFT'
            move(-step, 0)
        if pressed[pygame.K_RIGHT]:
            print 'pressed RIGHT'
            move(step, 0)
        if pressed[pygame.K_q]:
            print 'pressed Q'
            pygame.display.quit()
            sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mpos = pygame.mouse.get_pos()
        print 'click at ' + repr(mpos)
        walkto(mpos)	
    if moved:
        draw()
