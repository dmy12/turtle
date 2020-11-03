from turtle import *
from math import pi, sin, cos, sqrt

def flower(n=5,L0=50,colors=['gold','darkblue']):
    R=sqrt(5)/2*L0
    nn=60
    
    up()
    cc=((R+L0),0)
    goto(cc)
    seth(90)
    ii=0
    (x,y)=pos()
    while ii<nn and x-y*cos(pi/n)/sin(pi/n)>0:
        fd(2*pi/nn*R)
        left(360/nn)
        (x,y)=pos()
        ii=ii+1
    
    LL = abs(pos())
    tr = []
    k=0
    up()
    for i in range(n):
        cc=((R+L0)*cos(-2*pi/n*i+pi/n*k),(R+L0)*sin(-2*pi/n*i+pi/n*k))
        up()
        goto(cc)
        seth(-360/n*i+90+180/n*k)
            
        for ii in range(nn):
            if abs(pos())<LL:
                tr.append(pos())
            fd(2*pi/nn*R)
            left(360/nn)
        
    up()
    goto(tr[0])
    pencolor(colors[0])
    down()
    fillcolor(colors[1])
    begin_fill()
    begin_poly()
    for x in tr:
        '''
        if abs(pos())<L0/4:
            up()
        else:
            down()
        '''
        goto(x)
    goto(tr[0])
    end_poly()
    end_fill()
    
    p=get_poly()
    register_shape("flower",p)
    
    return 'flower'
    

def main():
    reset()
    setup(400,400)
    psize=2
    pensize(psize)
    speed(0)
    ht()
    
    n=5
    flower(n)
    shape('flower')
    color('gold','darkblue')
    shapesize(1,1,outline=psize)
    up()
    home()
    seth(180/n+90)
    stamp()
  
    return 'Done'
        

if __name__ == "__main__":
    main()
    mainloop()
