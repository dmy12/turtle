from turtle import *
from math import pi, sin, cos, sqrt
from random import randint
import time

        

def starpolygon(n=6,R=100,step=2,nface=2,center=(0,0),colors=['gold','darkblue']):
    if len(colors)>1:
        pencolor(colors[0])
        fillcolor(colors[1])
        
    a=2*pi/n
    v=[(R*cos(i*a)+center[0],R*sin(i*a)+center[1]) for i in range(n)]
    
    for j in range(nface):
        up()
        goto(v[j])
        down()
        if len(colors)>1:
            begin_fill()
        for i in range(1,n+1):
            goto(v[(j+i*step)%n])
            if (i*step)%n==0:
                break
        if len(colors)>1:       
            end_fill()
    
    return 'starpolygon'


    
def main():
    reset()
    setup(400,400)
    psize=2
    pensize(psize)
    speed(0)
    ht()
    n=Screen().numinput("Input", "num of vertices:", 8, minval=3, maxval=24)
    jump=Screen().numinput("Input", "jump:", 3, minval=1, maxval=12)
    nf=Screen().numinput("Input", "n face:", 1, minval=1, maxval=12)
    n=int(n)
    jump=int(jump)
    nf=int(nf)
    starpolygon(n=n,step=jump,nface=nf,colors=['gold','darkblue'])
    
    return 'Done'
        

if __name__ == "__main__":
    main()
    mainloop()