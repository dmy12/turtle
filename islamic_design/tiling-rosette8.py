#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from turtle import *
from math import pi, cos, sin, sqrt, fabs
from random import randint


    
def rosette8(n=8,r0=30,level=1,xo=1,
                     colors = ['black']*5):
    colormode(255)
    
    a=pi/n
    L=2*(1+sin(a))/sin(2*a)*r0
    x = r0/cos(a)
    xx = r0/sin(2*a)
    R = [r0/sin(a)-xx*sin(4*a)/sin(3*a),r0/sin(2*a),r0/sin(a)]
    
    s=Shape("compound")
    up()
    # petals
    color0=colors[1]
    for i in range(n):
        #up()
        goto((L*cos(2*a*i),L*sin(2*a*i)))
        seth(90+180/n+360/n*i)
        #down()
        begin_poly()
        fd(x)
        left(90-180/n)
        fd(x)
        left(360/n)
        fd(xx)
        left(180-720/n)
        fd(xx)
        left(360/n)
        fd(x)
        left(90-180/n)
        fd(x)
        end_poly()
        p=get_poly()
        s.addcomponent(p,color0,'white')
    
    
    if level>0:
        color0=colors[2]
        for i in range(n):
            p2 = (R[2]*cos(2*a*i+a),R[2]*sin(2*a*i+a))
            #up()
            goto(p2)
            #down()
            begin_poly()
            p1 = (R[1]*cos(2*a*i),R[1]*sin(2*a*i))
            goto(p1)
            p0 = (R[0]*cos(2*a*i+a),R[0]*sin(2*a*i+a))
            goto(p0)
            p1 = (R[1]*cos(2*a*i+2*a),R[1]*sin(2*a*i+2*a))
            goto(p1)
            goto(p2)
            end_poly()
            p=get_poly()
            s.addcomponent(p,color0,'white')
    
    #up()
    goto((R[0]*cos(a),R[0]*sin(a)))
    #down()
    
    if level>1 and level<=2:

        color0=colors[4]
        for i in range(0,n,n//4):
            #up() 
            goto(L*cos(2*a*(i+1)),L*sin(2*a*(i+1)))
            seth(360/n*(i+1)-(90-180/n))
            #down()
            xxx=L*(1-cos(2*a))/sin(3*a)
            begin_poly()
            fd(xxx)
            left(180-3*180/n)
            fd(L-xxx*2*cos(a))
            left(90)
            fd(L-xxx*2*cos(a))
            left(180-3*180/n)
            fd(xxx)
            
            for j in range(n//4-2):  
                fd(x)
                right(90-180/n)
                fd(x)
                left(180-360/n)
                fd(x)
                right(90-180/n)
                fd(x)
                right(360/n)
            
            end_poly()
            p=get_poly()
            s.addcomponent(p,color0,'white')
    
            
    if level>2:
        color0=colors[4]
        for i in range(0,n):
            #up() 
            goto(L*cos(2*a*(i+1)),L*sin(2*a*(i+1)))
            seth(360/n*(i+1)-(90-180/n))
            #down()
            begin_poly()
            for i in range(n):
                fd(x*xo)
                left(360/n)
            end_poly()
            p=get_poly()
            s.addcomponent(p,color0,'white')
    
    if level-int(level)==0.5:
        i=0
        p0 = (R[0]*cos(2*a*i+a),R[0]*sin(2*a*i+a))
        goto(p0)
        begin_poly()
        for i in range(n):
            p0 = (R[0]*cos(2*a*i+a),R[0]*sin(2*a*i+a))
            goto(p0)
        goto((R[0]*cos(a),R[0]*sin(a)))
        end_poly()
        p=get_poly()
        color0=colors[3]
        s.addcomponent(p,color0,'white')
    


    register_shape('rosette8', s)

       
def main():
    reset()
    setup(600,600)
    psize=5
    
    pensize(psize)
    
    ht()
    speed(0)
    
    #colors=[background,petals,sharpstar,polygon,angle around]
    fillcolors=[]
    for i in range(5):
        fillcolors.append((randint(0,255),randint(0,255),randint(0,255)))


    n=8
    r0 = 24
    level=Screen().numinput("Input", "level:", 1, minval=0, maxval=5)
    xo=1
    if level>2:
        xo=Screen().numinput("Input", "xo:", 1, minval=0, maxval=2)

    rosette8(n,r0,level,xo,colors=fillcolors)
    
    
    
  
    up()
    shapesize(1,outline=psize)   
    shape('rosette8')
    #home()
    #stamp()
    if level<=2:
        L=4*(1+sin(pi/n))/sin(2*pi/n)*r0+psize
        for i in range(-1,2):
            for j in range(-1,2):
                goto((i*L,j*L))
                seth(90)
                stamp()
    else:
        L=2*((1+sin(pi/n))/sin(pi/n))*r0
        L+=r0/cos(pi/n)*(1+sqrt(2))*xo
        for i in range(-1,2):
            for j in range(-1,2):
                goto((i*L,j*L))
                stamp()
        
        
    
        
    return "Done!"
        

if __name__ == "__main__":
    main()
    mainloop()
