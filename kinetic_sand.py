import pygame,sys
from pygame.locals import *
import math
width = 1000
height = 1000
num = 99
WHITE = (255,255,255)
windowSurface = pygame.display.set_mode((width, height))
points = []
windowSurface.fill((0,0,0))
pygame.init()
class Point():
    def __init__(self,x,y,m):
        self.x = float(x)
        self.y = float(y)
        self.m = m
        self.ix = x
        self.iy = y
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = 0.0
    def calc_force(self):
        cx,cy = pygame.mouse.get_pos()
        try:
            self.ax = (cx-self.x)*self.m/math.sqrt((cx-self.x)**2+(cy-self.y)**2)
        except ZeroDivisionError:
            pass
        try:
            self.ay = (cy-self.y)*self.m/math.sqrt((cx-self.x)**2+(cy-self.y)**2)
        except ZeroDivisionError:
            pass
        self.vx+=self.ax
        self.vy+= self.ay
        self.x +=self.vx
        self.y+=self.vy
    def go_back(self):
        self.vx = 10*(self.ix-self.x)/math.sqrt((self.ix-self.x)**2+(self.iy-self.y)**2)
        self.vy = 10*(self.iy-self.y)/math.sqrt((self.ix-self.x)**2+(self.iy-self.y)**2)
        self.x+= self.vx
        self.y+= self.vy
def show():
    for i in points:
        windowSurface.set_at((int(i.x),int(i.y)),WHITE)
for i in range(1,num+1):
    for l in range(1,num+1):
        points.append(Point(i*10,l*10,0.1))
while True:
    show()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if pygame.mouse.get_pressed()[0]== True:
        for i in points:
            i.calc_force()
    else:
        for i in points:
            if abs(i.ix -i.x) >10 and abs(i.iy -i.y) >10:
                i.go_back()
            else:
                i.x,i.y = i.ix,i.iy
                i.ax,i.ay,i.vx,i.vy = 0,0,0,0
    pygame.display.flip()
    windowSurface.fill((0,0,0))
