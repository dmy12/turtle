#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from turtle import *
from math import pi, cos, sin, sqrt, fabs
from random import randint
    
        
def rosette_p(n=12,r=20,R=120): 
    a=2*pi/n
    aa=180/n
    
    s=Shape("compound")
 
    l1=r/cos(a/2)
    l2=2*R-2*l1*sin(a/2)
    L=[l1,l2,l1]*2
    ta=[90-aa,90-aa,2*aa]*2
    v=[(0,0)]*n
    for i in range(n):
        v[i]=(R*cos(i*a),R*sin(i*a))
    #frame
    
    up()
    goto((0,-R))
    #down()
    begin_poly()
    circle(R,steps=n//2)
    up()
    goto((0,-(R+2*r/cos(a))))
    #down()
    circle(R+2*r/cos(a),steps=n//2)
    end_poly()
    p=get_poly()
    s.addcomponent(p,'purple','black')

    for i in range(n):
        up()
        goto(v[i])
        seth(90+aa+i*2*aa)
        #down()
        begin_poly()
        for j in range(len(L)):
            fd(L[j])
            left(ta[j])
        end_poly()
        p=get_poly()
        s.addcomponent(p,'purple','black')
    
    rr=r/sin(a/2)
    for i in range(n):
        v[i]=(rr*cos(i*a+a/2),rr*sin(i*a+a/2))
    up()
    goto(v[0])
    #down()
    begin_poly()
    for i in range(n+1):
        goto(v[(i*5)%n])
    end_poly()
    p=get_poly()
    s.addcomponent(p,'gold','black')
    
    x=2*r/(2+sqrt(2))
    r0=R*cos(a)-x/sqrt(2)
    
    for i in range(0,n,2):
        up()
        p0=(r0*cos(i*a),r0*sin(i*a))
        goto(p0)
        seth(i*2*aa+45)
        #down()
        begin_poly()
        for j in range(8):
            fd(x)
            left(45)
            fd(x)
            right(90)
        end_poly()
        p=get_poly()
        s.addcomponent(p,'gold','black')
    
    x=r/cos(a)
    for i in range(1,n+1,2):
        up()
        p0=(R*cos(i*a),R*sin(i*a))
        goto(p0)
        seth(i*2*aa+90+2*aa)
        #down()
        begin_poly()
        for j in range(n//2):
            fd(x)
            right(90+2*aa)
            fd(x)
            left(4*aa)
        end_poly()
        p=get_poly()
        s.addcomponent(p,'gold','black')
        
    register_shape('rosette_tile', s)
        
    
    
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
    

    n=12
    #(r,R)=(20,120),(10,120),(30,120)
    r=Screen().numinput("Input", "r:", 20, minval=0, maxval=300)
    R=Screen().numinput("Input", "R:", 120, minval=0, maxval=300)
    
    rosette_p(n,r,R)
    shapesize(1,outline=1)
    shape('rosette_tile')
    
    home()
    seth(90)
    stamp()
    R0=2*(R*sqrt(3)/2+r)
 
    for k in range(3):
        if k%2==0:
            R1=2**(k//2)*R0
        else:
            R1=R1*sqrt(3)
        for i in range(6):
            up()
            goto(R1*cos(2*pi/6*i+k*pi/6),R1*sin(2*pi/6*i+k*pi/6))
            stamp()

        
    return "Done!"
        

if __name__ == "__main__":
    main()
    time.sleep(10)
    bye()
