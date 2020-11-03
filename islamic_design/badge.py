from turtle import *
from math import pi, sin, cos
import time

def badge(n=3,L0=150,ratio=2.5):

    pencolor('gold')
    
    if n==3:
        for k in range(3):
            R=L0-4*k
            up()
            goto((0,-R))
            seth(0)
            circle(R,extent=90/n)
            down()
            r1 = R/3/sin(pi/n)
            for i in range(2*n):
                circle(r1,extent=85)
                up()
                circle(r1,extent=190)
                down()
                circle(r1,extent=85)
                up()
                circle(R,extent=180/n)
                down()
    
            
    for k in range(3):
        R=L0+4*k
        up()
        goto((0,-R))
        seth(0)
        down()
        circle(R)
        r2 = R/sin(pi/n)-2*R*sin(pi/n)/ratio #2.5 #can be changed
        
        for i in range(n):
            left(180/n)
            for j in range(2):
                fd(R/sin(pi/n)-r2)
                left(90)
                circle(-r2,extent=360/n)
                left(90)
                fd(R/sin(pi/n)-r2)
                left(360/n)
                
            right(180/n)
            circle(R,extent=180/n)
            
    return 'badge'

   
def main():
    reset()
    setup(400,400)
    bgcolor('black')
    pensize(2)
    speed(0)
    ht()
    
    n=Screen().numinput("Input", "num of sides:", 3, minval=3, maxval=24)
    L0=Screen().numinput("Input", "length:", 150, minval=50, maxval=200)
    ratio=Screen().numinput("Input", "ratio:", 2.5, minval=0.5, maxval=3)
    
    n=int(n)
    
    badge(n=n,L0=L0,ratio=ratio)
    
    return 'Done'
  

if __name__ == "__main__":
    main()
    mainloop()
