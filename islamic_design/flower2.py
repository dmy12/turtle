from turtle import *
from math import pi, sin, cos, sqrt
from random import randint

def flower2(n=8,R=[200,195,160,100,60]):
    
    p0=[]
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    a=pi/n
    for i in range(n+1):
        p0.append((R[0]*cos(2*a*i),R[0]*sin(2*a*i)))
        p1.append((R[1]*cos(2*a*i-a/2),R[1]*sin(2*a*i-a/2)))
        p1.append((R[1]*cos(2*a*i+a/2),R[1]*sin(2*a*i+a/2)))
        p2.append((R[2]*cos(2*a*i-a),R[2]*sin(2*a*i-a)))
        p3.append((R[3]*cos(2*a*i),R[3]*sin(2*a*i)))
        p4.append((R[4]*cos(2*a*i-a),R[4]*sin(2*a*i-a)))
    
    for i in range(n):
        up()
        goto(p0[i])
        down()
        goto(p1[2*i])
        goto(p2[i])
        goto(p3[i])
        goto(p2[i+1])
        goto(p1[2*i+1])
        goto(p0[i])
    
    
    for i in range(n):
        up()
        goto(p2[i%n])
        down()
        goto(p3[(i-1)%n])
        goto(p4[i%n])
        goto(p3[i%n])
        goto(p2[i%n])
        
        
        
    
def main():
    reset()
    setup(400,400)
    pensize(1)
    speed(0)
    ht()
    
    flower2()
    return 'Done'
        

if __name__ == "__main__":
    main()
    mainloop()
