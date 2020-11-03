from turtle import *
from math import sqrt

def SAVEPIC():
    canvas = getscreen().getcanvas()
    canvas.postscript(file='turtle_graphic_example' + '.eps')

def GRID4(L0=20,W=600,H=600):
    colormode(255)
    color0 = (180,180,180)
    pencolor(color0)
    
    m,n=W//(2*L0),H//(2*L0)
    
    for i in range(-n,n+1):
        up()
        goto((-m*L0,i*L0))
        seth(0)
        down()
        fd(W)
    for i in range(-m,m+1):
        up()
        goto((i*L0,-n*L0))
        seth(90)
        down()
        fd(H)
        
def GRID3(L0=20):
    colormode(255)
    color0 = (180,180,180)
    pencolor(color0)
    for i in range(-15,16):
        up()
        goto(-300,i*L0*sqrt(3)/2)
        seth(0)
        down()
        fd(620)
    for i in range(-20,20):
        up()
        goto(i*L0,-10*L0*sqrt(3)/2)
        seth(60)
        down()
        fd(800) 
        
        up()
        goto(i*L0,-10*L0*sqrt(3)/2)
        seth(120)
        down()
        fd(800) 
        
        
def HOME():
    up()
    home() 
def LEFT():
    seth(180)
    fd(L0)
def RIGHT():
    seth(0)
    fd(L0)
def UP():
    seth(90)
    fd(L0)
def DOWN():
    seth(-90)
    fd(L0)
def UP3():
    seth(60)
    fd(L0)
def DOWN3():
    seth(240)
    fd(L0)
    

    
def onkeyops(mode=3):
    screen = Screen()
    screen.onkey(HOME,'h')
    
    screen.onkey(LEFT,'Left')
    screen.onkey(RIGHT,'Right')
    if mode==3:
        screen.onkey(GRID3,'g')
        screen.onkey(UP3,'Up')
        screen.onkey(DOWN3,'Down')
    else:
        screen.onkey(GRID4,'g')
        screen.onkey(UP,'Up')
        screen.onkey(DOWN,'Down')
    screen.onkey(undo,'u')
    screen.onkey(clear,'c')
    screen.onkey(SAVEPIC,'s')
    #screen.listen()
     

    
