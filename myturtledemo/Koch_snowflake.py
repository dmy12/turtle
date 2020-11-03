from turtle import *
from math import pi,sin,cos,tan

def koch_1side(depth=0,L=300,direction = 1,
               angle = [60,240,60,0]):
    if depth==0:
        forward(L)
    else:
        for i in range(4):
            koch_1side(depth-1,L/3,direction,angle)
            right(angle[i]*direction)
        
def koch_snowflake(depth=0,L=300,direction=1, n=3,
                   angle=[60,240,60,0]):
    
    for i in range(n):
        koch_1side(depth,L,direction,angle)
        left(360/n)
        
def main():
    reset()
    W = 600
    H = 600
    screensize(W,H)
    speed(0)
    clear()
    
    L=100
    
    n=Screen().numinput("Input", "Sides:", 3, minval=3, maxval=24)
    depth=Screen().numinput("Input", "Depth:", 2, minval=1, maxval=5)
    direction = Screen().numinput("Input", "Direction 1 or -1:", 1, minval=-1, maxval=1)
    n=int(n)
    depth=int(depth)
    direction=int(direction)
    
    aa = 180/n
    angles = [aa,360-2*aa,aa,0]

    nL = ((3+3*cos(pi/n))/n)**depth*L
    
    penup()
    goto((-nL*cos(pi/n),-nL*cos(pi/n)/tan(pi/n)))
    pendown()
    if direction==0:
        koch_snowflake(depth,nL,1,n,angles)
        penup()
        goto((-nL*cos(pi/n),-nL*cos(pi/n)/tan(pi/n)))
        pendown()
        koch_snowflake(depth,nL,-1,n,angles)
    else:
        koch_snowflake(depth,nL,direction,n,angles)
    
    ht()


    return "Done!"

if __name__ == "__main__":

    main()
    mainloop()