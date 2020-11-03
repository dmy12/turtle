from turtle import *
from math import pi, sin, cos, sqrt
from random import randint


def polygon6(L=50,aa=45):
    a=[aa,120-aa]*3
    for i in range(6):
        fd(L)
        left(a[i])
        
def star6(L=50,aa=60):
    n=6
    p = []
    LL=2*L*cos(aa*pi/180/2)
    a=2*pi/n
    for i in range(n):
        p.append((LL*cos(a*i),LL*sin(a*i)))
        
    for i in range(len(p)):
        up()
        goto(p[i])
        seth(360/n*i+60-aa/2)
        down()
        polygon6(L,aa)

        
def star6_tiling(L=25,aa=60):
    n=6
    fillcolor('darkblue')
    centers=[(0,0)]
    LL=2*L*cos(aa*pi/180/2)
    a=2*pi/n
    for i in range(n):
        centers.append((2*LL*cos(a*i),2*LL*sin(a*i)))
    
    for j in range(len(centers)):
        p = []
        for i in range(n):
            p.append((centers[j][0]+LL*cos(a*i), centers[j][1]+LL*sin(a*i)))
            
            
        for i in range(len(p)):
            up()
            goto(p[i])
            seth(360/n*i+60-aa/2)
            down()
            begin_fill()
            polygon6(L,aa)
            end_fill()
           
def main():
    reset()
    setup(400,400)
    pensize(1)
    speed(0)
    ht()
    
    aa=Screen().numinput("Input", "adjust polygon6 aa(-60~120):", 60, minval=-360, maxval=360)

    star6_tiling(aa=aa)
    
    return 'Done'
        

if __name__ == "__main__":
    main()
    mainloop()
