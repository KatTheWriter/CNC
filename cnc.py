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
barheight = 75
step = 5
moved = 0

displaylist = [
        {
            "name": "garden",
            "type": "border",
            "colour": 0x22ee22,
            "location": pygame.Rect(0,0, 800,600)
        },
        {
            "name": "shed",
            "type": "obstacle",
            "colour": 0xbbbbbb,
            "location": pygame.Rect(565,0, 245,125)
        },
        {
            "name": "menubar",
            "type": "obstacle",
            "colour": 0xffffff,
            "location": pygame.Rect(0,600-barheight, 800,600)
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

def overlap(rect, x, y, width, height):
    print("rect top=" + repr(rect.top) + ",left=" + repr(rect.left) + ",bottom=" + repr(rect.bottom) + ",right=" + repr(rect.right))
    ret = (x < rect.right and x+width > rect.left and y+height > rect.top and y < rect.bottom)
    print("overlap " + repr(rect) + "," + repr(x) + "," + repr(y) + "," + repr(width) + "=>" + repr(ret))
    return ret

def inside(rect, x, y, width, height):
    print("rect top=" + repr(rect.top) + ",left=" + repr(rect.left) + ",bottom=" + repr(rect.bottom) + ",right=" + repr(rect.right))
    ret = (x+width < rect.right and x > rect.left and y > rect.top and y+height < rect.bottom)
    print("overlap " + repr(rect) + "," + repr(x) + "," + repr(y) + "," + repr(width) + "=>" + repr(ret))
    return ret
    
def move(dx,dy):
    global x, y, moved
    nx = x + dx
    ny = y + dy

    # objects
    for obj in displaylist:
        if (obj["type"] == "obstacle" and overlap(obj["location"], nx, ny, bodsize, bodsize)):
            print 'Keep out of the ' + obj["name"] + ', Bod'
            return
        if (obj["type"] == "border" and not inside(obj["location"], nx, ny, bodsize, bodsize)):
            print 'Stay in the ' + obj["name"] + ', Bod'
            return

    x = nx
    y = ny
    moved = 1

def walkto(pos):
    global x, y, moved
    print 'Moving to (' + repr(pos[0]) + ',' + repr(pos[1]) + ')'
    dx = pos[0] - x
    dy = pos[1] - y
    move(dx,dy)

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
