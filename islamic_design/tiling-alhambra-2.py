'''
ID | Method
0  | method=0
1  | method=1
2  | method=2
3  | method=1
4  | method=4
5  | method=3
'''


from turtle import *
from myscreenevents import onkeyops
from tile3 import Tiles3
from math import pi, sin, cos, sqrt
from random import randint


def STAMP0():
    color('white',colors[0])
    stamp()
def SPIN():
    left(30)
    
   
def onkeyops1(tilingmode=3):
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
    


# tiling style 0
def AddTiles0():
    n=W//(4*L0)
    up()
    centers=[]
    
    for i in range(-n-1,n+1):
        for j in range(-n-1,n+1):
            centers.append(((2.5*j+0.5*i)*L0,sqrt(3)/2*(j+3*i)*L0))
    
    right(90)
    for cc in centers:
        k = randint(0,len(colors)-1)
        color('white',colors[k])
        goto(cc)
        stamp()
        
    return

# style 1
def AddTiles1():
    n=W//(4*L0)
    up()
    
    centers1=[]
    centers2=[]
    for i in range(-n-1,n+1):
        for j in range(-n-1,n):
            centers1.append(((4*j+2*i)*L0,sqrt(3)/2*(4*i)*L0))
            centers2.append(((4*j+2*i+2.5)*L0,sqrt(3)/2*(4*i-1)*L0))
            
    
    right(30)
    for cc in centers1:
        k = randint(0,len(colors)-1)
        color('white',colors[k])
        goto(cc)
        stamp()
    right(60)
    for cc in centers2:
        k = randint(0,len(colors)-1)
        color('white',colors[k])
        goto(cc)
        stamp()    
    return

# style 2
def AddTiles2():
    n=W//(4*L0)
    up()
    
    centers1=[]
    centers2=[]
    for i in range(-n-1,n+1):
        for j in range(-n-1,n):
            centers1.append(((5*j+2.5*i)*L0,sqrt(3)/2*(5*i)*L0))
            centers2.append(((5*j+2.5*i+3)*L0,sqrt(3)/2*(5*i+2)*L0))
            
    
    right(30)
    for cc in centers1:
        k = randint(0,len(colors)-1)
        color('white',colors[k])
        goto(cc)
        stamp()
    right(60)
    for cc in centers2:
        k = randint(0,len(colors)-1)
        color('white',colors[k])
        goto(cc)
        stamp()    
    return

# style 3
def AddTiles3():
    n=W//(4*L0)
    up()
    centers=[]
    
    right(30)
    for i in range(-n-1,n+1):
        for j in range(-n-1,n+1):
            centers.append(((3*j)*L0,sqrt(3)/2*(2*j+4*i)*L0))
    
    right(90)
    for cc in centers:
        k = randint(0,len(colors)-1)
        color('white',colors[k])
        goto(cc)
        stamp()
        
    return

# style 4
def AddTiles4():
    n=W//(4*L0)
    up()
    
    centers1=[]
    centers2=[]
    for i in range(-n-1,n+1):
        for j in range(-n-1,n+1):
            centers1.append(((6*j-3*i)*L0,sqrt(3)/2*(6*i)*L0))
          
    for cc in centers1:
        for i in range(6):
            cc2=(cc[0]+2*sqrt(3)*L0*cos(pi/3*i+pi/6),cc[1]+2*sqrt(3)*L0*sin(pi/3*i+pi/6))
            centers2.append(cc2)
    right(30)
    for cc in centers2:
        goto(cc)
        right(60)
        k = 0#randint(0,len(colors)-1)
        color('white',colors[k])
        stamp()
        
        right(120)
        k = 0#randint(0,len(colors)-1)
        color('white',colors[k])
        
        stamp() 
        
        right(120)
        k = 0#randint(0,len(colors)-1)
        color('white',colors[k])
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
    for i in range(5):
        rint=randint(0,220)
        color0=((randint(0,200),randint(0,200),randint(0,200)))
        #color0=(randint(0,255),randint(0,255),randint(0,255))
        colors.append(color0)
    
    ht()
    tracer(0)
    speed(0)
    
    i=Screen().numinput("Input", "Id(0~5):", 0, minval=0, maxval=7)

    onkeyops1(3)
    
    up()
    home()
    seth(0)

    Tiles3(i)
    shape("Tile3_"+str(i))


    return "Done!"   

if __name__ == "__main__":
    main()
    mainloop()
    bye()


