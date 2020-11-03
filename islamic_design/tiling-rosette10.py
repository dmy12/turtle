#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from turtle import *
from math import pi, cos, sin, sqrt, fabs
from random import randint

    
def rosette_10(n=10,r0=30,level=1,fortiling = False,colors=['black']*5):
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
        color0=(randint(40,200),randint(40,200),randint(40,200))
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
            color0=(randint(40,200),randint(40,200),randint(40,200))
        
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

    if level>1:
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
    
    
    if fortiling==True:
        color0=colors[1]
        iv=[3,8]
        for i in iv:
            color0=(randint(40,200),randint(40,200),randint(40,200))
            goto((L*cos(2*a*i),L*sin(2*a*i)))
            seth(-90+180/n+360/n*i)
            begin_poly()
            fd(xx)
            left(180-720/n)
            fd(xx)
            left(360/n)
            fd(x)
            left(90-180/n)
            fd(x)
            left(360/n)
            fd(x)
            left(90-180/n)
            fd(x)
            end_poly()
            p=get_poly()
            s.addcomponent(p,color0,'white')

            

    register_shape("rosette10", s)
    
    return   

       
def main():
    reset()
    setup(600,600)
    psize=1
    
    pensize(psize)
    
    ht()
    speed(0)
    
    #colors=[background,petals,sharpstar,polygon,angle around]
    fillcolors=[]
    for i in range(5):
        fillcolors.append((randint(0,255),randint(0,255),randint(0,255)))

    r0=20
    n=10
    level=1
    a=pi/n
    L=2*(1+sin(a))/sin(2*a)*r0
    tracer(0)
    level=Screen().numinput("Input", "Tile details:", 1, minval=0, maxval=7)

    if Screen().textinput("Input", "Tiling?(Y/N)") == "Y":
        iftiling=True
    else:
        iftiling=False
    
    rosette_10(n,r0,level,iftiling,colors=fillcolors)
    shape("rosette10")
    home()
    stamp()
    if iftiling==True:
        (x,y)=(2*L*sin(2*pi/n),2*L*sin(3*pi/n))
        for i in range(-2,3):
            for j in range(-2,3):
                goto(((2*i+j)*x,j*y))
                stamp()
           
    return "Done!"
        

if __name__ == "__main__":
    main()
    mainloop()
