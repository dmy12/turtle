from turtle import *
from math import pi, sin, cos, sqrt

def star10(R=150):
    n=10
    a=pi/n
    aa=180/n
    pencolor('gold')
    fillcolor('darkblue')
    # can change L1,L2
    L1=2*R*sin(3*a)*sin(a)
    L2=2*R*sin(2*a)*sin(3*a)/(1+sin(3*a))-5

    v0=(R,0)
    
    up()
    goto(v0)
    seth(180-2*aa)
    down()
    
    begin_fill()
    for i in range(n):
        fd(L1)
        left(90)
        fd(L2)
        left(2*aa)
        fd(L2)
        left(90)
        fd(L1)
        left(180-4*aa)
    end_fill()
                
    return 'star10'

def main():
    reset()
    setup(400,400)
    pensize(5)
    speed(0)
    ht()
    star10()
    return 'Done'
        

if __name__ == "__main__":
    main()
    mainloop()
