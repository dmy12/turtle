from turtle import *
from math import pi, sin, cos, sqrt

def Tiles3(id=0,L0=20):
    if id==0:
        L=[1,1,1]*3
        L=[x*L0 for x in L]
        a=[60,-60,120]*3
        
        begin_poly()
        for i in range(len(L)):
            fd(L[i])
            left(a[i])
        end_poly()
        p = get_poly() 
    elif id==1:
        L=[2,1,1]*3
        L=[x*L0 for x in L]
        a=[120,60,-60]*3
        begin_poly()
        for i in range(len(L)):
            fd(L[i])
            left(a[i])
        end_poly()
        p = get_poly() 
    elif id==2:
        L=[2,1,1,1,1,1]*3
        L=[x*L0 for x in L]
        a=[60,60,60,120,-120,-60]*3
        begin_poly()
        for i in range(len(L)):
            fd(L[i])
            left(a[i])
        end_poly()
        p = get_poly() 
    elif id==3:
        L=[2,sqrt(3)]*3
        L=[x*L0 for x in L]
        a=[150,-30]*3
        begin_poly()
        for i in range(len(L)):
            fd(L[i])
            left(a[i])
        end_poly()
        p = get_poly() 
    elif id==4:
        L=[1,3,3,1,1,1]
        L=[x*L0 for x in L]
        a=[120,120,120,60,-120,60]
        begin_poly()
        for i in range(len(L)):
            fd(L[i])
            left(a[i])
        end_poly()
        p = get_poly() 
    elif id==5:
        L=L0
        begin_poly()
        for i in range(3):
            circle(L,extent=120)
            circle(-L,extent=120)
            left(120)
        end_poly()
        p = get_poly()
    
    addshape('Tile3_'+str(id),p)
    
    return 'Tile3_'+str(id)

 
def main():
    reset()
    setup(400,400)
    pensize(1)
    speed(0)
    ht()
    
    i=Screen().numinput("Tile", "Index(0-5):", 0, minval=0, maxval=5)
    i=int(i)
    Tiles3(i)
    
    return 'Done'
        

if __name__ == "__main__":
    main()
    mainloop()
