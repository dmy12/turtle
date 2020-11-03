#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from turtle import *
from math import pi, cos, sin, sqrt
from random import randint
import time




    
def rosette_parallel(n=8,r0=30,level=1, 
                     colors = ['black']*5,stampname='rosette'):
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
    
    
    if level>1:
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

    register_shape(stampname, s)
    
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
    n=Screen().numinput("Input", "n:", 12, minval=3, maxval=36)
    level=Screen().numinput("Input", "level:", 1.5, minval=0, maxval=4)
    n=int(n)
    rosette_parallel(n,r0,level,fillcolors,'rosette')
    shape('rosette')
    up()
    home()
    stamp()
           
    return "Done!"
        

if __name__ == "__main__":
    main()
    mainloop()