'''
ID | Method
0  | p*2(left(30)), method=1
1  | p*3(left(45)), method=1
2  | method=0
3  | method=0
4  | method=2
5  | method=2
6  | method=4
7  | method=3
'''


from turtle import *
from myscreenevents import onkeyops
from tile4 import Tiles4
from math import pi, sin, cos, sqrt
from random import randint


def STAMP0():
    color('white',colors[0])
    stamp()
def SPIN():
    left(15)
    
def onkeyops1(tilingmode=4):
    screen = Screen()
    onkeyops(mode=tilingmode)
    screen.onkey(STAMP0,'=')
    screen.onkey(SPIN,'p')
    screen.onkey(AddTiles0,'0')
    screen.onkey(AddTiles1,'1')
    screen.onkey(AddTiles2,'2')
    screen.onkey(AddTiles3,'3')
    screen.onkey(AddTiles4,'4')
    screen.listen()
    
    
# chess board style 0
def AddTiles0():
    n=W//(8*L0)
    up()
    centers1=[]
    centers2=[]
    for i in range(-n-1,n+1):
        for j in range(-n-1,n+1):
            centers1.append((2*L0+4*j*L0,4*i*L0+2*L0))
            #centers2.append((2*L0+4*j*L0,4*i*L0+2*L0))
            centers2.append((4*j*L0,4*i*L0))
    
    color('white',colors[0])
    for cc in centers1:
        goto(cc)
        stamp()

    right(180)
    color('white',colors[1])
    for cc in centers2:
        goto(cc)
        stamp()
    
    return

# chess board style 1
def AddTiles1():
    n=W//(8*L0)
    up()
    centers1=[]
    centers2=[]
    for i in range(-n-1,n+1):
        for j in range(-n-1,n+1):
            centers1.append((2*L0+4*j*L0,4*i*L0+2*L0))
            centers2.append((2*L0+4*j*L0,4*i*L0+2*L0))
            #centers2.append((4*j*L0,4*i*L0))
    
    color('white',colors[0])
    for cc in centers1:
        goto(cc)
        stamp()

    right(180)
    color('white',colors[1])
    for cc in centers2:
        goto(cc)
        stamp()
    
    return

# chess board style 2
def AddTiles2():
    n=W//(8*L0)
    up()
    centers1=[]
    centers2=[]
    for i in range(-n-1,n+1):
        for j in range(-n-1,n+1):
            centers1.append((8*j*L0,8*i*L0))
            centers1.append((4*L0+8*j*L0,4*L0+8*i*L0))
            centers2.append((8*j*L0,4*L0+8*i*L0))
            centers2.append((4*L0+8*j*L0,8*i*L0))
    
    #seth(aa/2)
    color('white',colors[0])
    for cc in centers1:
        goto(cc)
        stamp()

            
    #seth(aa/2+180)
    right(180)
    color('white',colors[1])
    for cc in centers2:
        goto(cc)
        stamp()
    
    return

# chess board style 3
def AddTiles3():
    n=W//(8*L0)
    up()
    centers1=[]
    centers2=[]
    for i in range(-n-1,n+1):
        for j in range(-n-1,n+1):
            centers1.append((6*j*L0,6*i*L0))
            centers1.append((3*L0+6*j*L0,3*L0+6*i*L0))
            centers2.append((6*j*L0,3*L0+6*i*L0))
            centers2.append((3*L0+6*j*L0,6*i*L0))
    
    #seth(aa/2)
    color('white',colors[0])
    for cc in centers1:
        goto(cc)
        stamp()

    right(90)        
    #seth(aa/2+180)
    color('white',colors[1])
    for cc in centers2:
        goto(cc)
        stamp()
    
    return

# chess board style 4
def AddTiles4():
    n=W//(8*L0)
    up()
    centers1=[]
    centers2=[]
    for i in range(-n-1,n+1):
        for j in range(-n-1,n+1):
            centers1.append((6*j*L0,6*i*L0))
            centers2.append((6*j*L0+2*L0,6*i*L0+2*L0))
    
    #seth(aa/2)
    color('white',colors[0])
    for cc in centers1:
        goto(cc)
        stamp()
        
    #seth(aa/2+180)
    right(180)
    color('white',colors[1])
    for cc in centers2:
        goto(cc)
        stamp()
    
    return


def main():
    reset()
    
    global W, H, L0, colors
    W=600
    H=600
    L0=20
    
    setup(W,H)
    
    colormode(255)
    colors=[]
    for i in range(4):
        rint=randint(0,220)
        color0=(rint,rint,rint)
        #color0=(randint(0,255),randint(0,255),randint(0,255))
        colors.append(color0)
    
    ht()
    tracer(0)
    speed(0)
    
    i=Screen().numinput("Input", "Id(0~7):", 0, minval=0, maxval=7)

    onkeyops1(4)
    
    up()
    home()
    seth(0)
    
    Tiles4(i)
    shape("Tile4_"+str(i))


    return "Done!"   

if __name__ == "__main__":
    main()
    mainloop()
    