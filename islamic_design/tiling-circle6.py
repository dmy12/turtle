from turtle import *
from math import pi, sin, cos, sqrt
        
def circle612(L=50,aa=0,center=(0,0)):
    
    colors=['#c4cbcf','#541e24']
    
    LL=L/2/cos(aa/2*pi/180)
    
    a6=[aa,120-aa]*3
    a8=[aa,90,360-aa,90]*2
    
    for i in range(6):
        a=i*60
        up()
        goto((center[0]+L*cos((a+30)*pi/180),center[1]+L*sin((a+30)*pi/180)))
        down()

        seth(a-aa/2)
        
        fillcolor(colors[0])
        begin_fill()
        for j in range(6):
            fd(LL)
            left(a6[j])
        end_fill()
        
        right(90)
        
        fillcolor(colors[1])
        begin_fill()
        for j in range(8):
            fd(LL)
            left(a8[j])
        
        end_fill()

def circle612_tiling(L=20,aa=0):
    centers={(0,0)}
    LL=L+sqrt(3)*L
    for i in range(6):
        a=2*pi/6*i
        centers.add((LL*cos(a),LL*sin(a)))
    
    for xy in centers:
        circle612(L,aa,xy)
           
def main():
    reset()
    setup(400,400)
    pensize(1)
    speed(0)
    ht()
    
    aa=Screen().numinput("Input", "adjust triangle aa(-60~120):", 0, minval=-360, maxval=360)
    circle612_tiling(aa=aa)
    
    return 'Done'
        

if __name__ == "__main__":
    main()
    mainloop()
