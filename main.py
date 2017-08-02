from pygame import*
from math import*
import Ball

screen=display.set_mode((1500,500),SRCALPHA)
display.set_caption("Ping Pong")

floorRect = Rect(0,450,1500,50)
netRect = Rect(740,375,20,75)

p1x=0
p1y=100
player1Paddle = Rect(p1x,p1y,15,75)
p1PaddleUp = False
p1PaddleDown = False
p1score=0

p2x=1485
p2y=100
player2Paddle = Rect(p2x,p2y,15,75)
p2PaddleUp = False
p2PaddleDown = False
p2score=0

mainBall = Ball.Ball(screen,100,100,20,floorRect,netRect)

paddle = None

clock = time.Clock()
font.init()
myfont = font.SysFont('Calibri', 30)



# CHANGE THIS TO TURN AUTO MODE ON AND OFF
#
#
#
autoMode = True
#
#
#
#

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

        if not autoMode:
            if e.type == KEYDOWN:
                #Player 1 controls
                if e.key == K_w:
                    p1PaddleUp = True
                    p1PaddleDown = False
                if e.key == K_s:
                    p1PaddleUp = False
                    p1PaddleDown = True
                    # Player 2 controls
                if e.key == K_UP:
                    p2PaddleUp = True
                    p2PaddleDown = False
                if e.key == K_DOWN:
                    p2PaddleUp = False
                    p2PaddleDown = True

            if e.type == KEYUP:
                # Player 1 controls
                if e.key == K_w:
                    p1PaddleUp = False
                if e.key == K_s:
                    p1PaddleDown = False
                # Player 2 controls
                if e.key== K_UP:
                    p2PaddleUp = False
                if e.key ==K_DOWN:
                    p2PaddleDown = False


    screen.fill((255,255,255))

    if autoMode:
        if mainBall.x < 750:
            if mainBall.y < p1y + 10:
                p1y -=10
            elif mainBall.y > p1y + 65:
                p1y += 10

        if mainBall.x > 750:
            if mainBall.y < p2y + 10:
                p2y-=10
            elif mainBall.y > p2y + 65:
                p2y += 10


    if p1PaddleUp:
        if p1y > 0:
            p1y -= 10
    elif p1PaddleDown:
        if p1y < 375:
            p1y += 10

    if p2PaddleUp:
        if p2y > 0:
            p2y -= 10
    elif p2PaddleDown:
        if p2y < 375:
            p2y += 10






    player1Paddle = Rect(p1x, p1y, 15, 75)
    player2Paddle = Rect(p2x, p2y, 15, 75)

    paddleChange = mainBall.control(player1Paddle,player2Paddle)
    if paddleChange is not None:
        paddle = paddleChange

    if mainBall.x+ mainBall.diameter + 100 < 0:
        mainBall = Ball.Ball(screen, 1400, 100, 20, floorRect, netRect, startRight=False)
        p2score +=1

    if mainBall.x-100>  1500:
        mainBall = Ball.Ball(screen, 100, 100, 20, floorRect, netRect)
        p1score += 1


    if mainBall.dead:
        if paddle == "left":
            mainBall = Ball.Ball(screen, 1400, 100, 20, floorRect, netRect, startRight=False)
            p2score += 1
        elif paddle == "right":
            mainBall = Ball.Ball(screen, 100, 100, 20, floorRect, netRect)
            p1score += 1
        else:
            mainBall.dead = False

    p1score_dis= myfont.render(str(p1score) ,True,(255,255,255))
    p2score_dis = myfont.render(str(p2score) , True, (255, 255, 255))

    mainBall.display()
    draw.rect(screen,(0,0,0),floorRect,0)
    draw.rect(screen, (0, 0, 0), netRect, 0)
    draw.rect(screen,(0,0,0),player1Paddle,0)
    draw.rect(screen, (0, 0, 0), player2Paddle, 0)
    screen.blit(p1score_dis,(750 - p1score_dis.get_width()-53,460))
    screen.blit(p2score_dis, (750 + 50, 460))

    display.flip()
    clock.tick(60)

quit()

