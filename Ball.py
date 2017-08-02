from pygame import *
import random

class Ball:
    mainSurface = None;
    x = y = 0

    diameter = 0

    mainRect = None

    velocity = 3

    floorRect = None
    netRect = None

    goingUp = False
    goingDown = True
    goingRight = True
    goingLeft = False

    oldPositions = []

    dead = False

    acceleration = 0.2

    def __init__(self,surface : Surface, x:int, y:int,diameter:int,floor:Rect,net:Rect,startRight = True):
        self.mainSurface = surface
        self.x = x
        self.y = y
        self.diameter = diameter

        self.floorRect = floor

        self.oldPositions = [(x,y) for x in range(10)]

        self.netRect = net

        self.setRects()

        self.goingRight = startRight
        self.goingLeft = not startRight

    def setRects(self):
        self.mainRect = Rect(self.x,self.y,self.diameter,self.diameter)

    def control(self,leftPaddle : Rect,rightPaddle : Rect):

        del self.oldPositions[0]
        self.oldPositions.append((self.x,self.y))

        if self.goingDown:
            if self.mainRect.colliderect(self.floorRect):
                self.goingDown = False
                self.goingUp = True
            else:
                self.velocity += self.acceleration
                self.y += self.velocity


        if self.goingUp:
            if self.velocity <= 0:
                self.velocity = 0
                self.goingUp = False
                self.goingDown = True
            else:
                self.velocity -= self.acceleration
                self.y -= self.velocity

        if self.goingRight:
            for x in range(10):
                self.x+=1
                if rightPaddle.colliderect(self.mainRect):
                    self.velocity = random.randint(1,10)
                    self.goingRight = False
                    self.goingLeft = True
                    self.goingUp = True
                    self.goingDown = False
                    self.setRects()
                    return "right"
                    break

        if self.goingLeft:
            for x in range(10):
                self.x-=1
                if leftPaddle.colliderect(self.mainRect):
                    self.velocity = random.randint(1, 10)
                    self.goingRight = True
                    self.goingLeft = False
                    self.goingUp = True
                    self.goingDown = False
                    self.setRects()
                    return "left"
                    break

        if self.netRect.colliderect(self.mainRect):
            self.dead = True

        self.setRects()

    def display(self):
        count = 0
        for pos in self.oldPositions:
            draw.circle(self.mainSurface,(int(255 - 25 * count),int(255 - 18 * count),int(255 - 18*count)),[int(pos[0]),int(pos[1])],self.diameter//2,0)
            count += 1

            draw.circle(self.mainSurface, (200, 50, 50),
                        [int(self.oldPositions[len(self.oldPositions)-1][0]), int(self.oldPositions[len(self.oldPositions)-1][1])], self.diameter // 2, 0)

