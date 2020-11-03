from turtle import *
from math import pi, sin, cos, sqrt

def Tiles4(id=0,L0=20,ifdraw=False):
    if id==0:
        aa=60
        LL=L0/cos(aa/2*pi/180)
        L = [LL]*8
        a = [360-aa,90,aa,90]*2

        begin_poly()
        for i in range(len(L)):
            fd(L[i])
            left(a[i])
        end_poly()
        p = get_poly()   
    elif id==1:
        r=sqrt(2)*L0
        
        begin_poly()
        circle(r,extent=90)
        left(90)
        circle(-r,extent=90)
        left(90)
        circle(r,extent=90)
        left(90)
        circle(-r,extent=90)
        left(90)
        end_poly()
        p=get_poly()
    elif id==2:
        LL=L0/2
        p=((LL,-LL),(2*LL,-2*LL),(3*LL,-LL),(3*LL,LL),(2*LL,2*LL),(LL,LL),
           (-LL,LL),(-2*LL,2*LL),(-3*LL,LL),(-3*LL,-LL),(-2*LL,-2*LL),(-LL,-LL))
    elif id==3:
        LL=L0/2
        p=((0,-3*LL),(LL,-2*LL),(2*LL,-2*LL),(2*LL,-LL),(LL,0),(2*LL,LL),(2*LL,2*LL),(LL,2*LL),
           (0,3*LL),(-LL,2*LL),(-2*LL,2*LL),(-2*LL,LL),(-LL,0),(-2*LL,-LL),(-2*LL,-2*LL),(-LL,-2*LL))
    elif id==4:
        LL=2*L0
        p=((0,-LL),(LL,-LL/2),(LL,0),(LL/2,0),(0,LL),(-LL/2,0),(-LL,0),(-LL,-LL/2))
    elif id==5:
        LL=L0
        p=((0,-2*LL),(LL,-1.5*LL),(LL,-LL),(2*LL,0),(LL,LL),(0.5*LL,LL),(0,2*LL),
        (-0.5*LL,LL),(-LL,LL),(-2*LL,0),(-LL,-LL),(-LL,-1.5*LL))
    elif id==6:
        LL=L0
        p=((-LL,LL),(0,LL),(LL,2*LL),(LL,LL),(2*LL,LL),(2*LL,0),(LL,0),(2*LL,-LL),(2*LL,-2*LL),
           (LL,-2*LL),(0,-LL),(0,-2*LL),(-LL,-2*LL),(-LL,-LL),(-2*LL,-LL),(-LL,0))
    elif id==7:
        LL=L0
        p=((0,-LL),(2*LL,0),(0,LL),(-2*LL,0))
    
    if ifdraw==True and id>=2:
        up()
        goto(p[0])
        down()
        for i in range(len(p)):
            goto(p[i])
        goto(p[0])
        
    addshape('Tile4_'+str(id),p)
    
    return 'Tile4_'+str(id)
    
    
def main():
    reset()
    setup(400,400)
    pensize(1)
    speed(0)
    ht()
    
    i=Screen().numinput("Tile", "Index(0-7):", 0, minval=0, maxval=7)
    i=int(i)
    Tiles4(i,ifdraw=True)
    
    return 'Done'
        

if __name__ == "__main__":
    main()
    mainloop()
