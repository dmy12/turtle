
from turtle import *

def spiral_line(angle = 90, 
                L=4,Lplus=2,N=100,
                startpoint=(0,0), colorlist= []):
    penup()
    goto(startpoint)
    pendown()
    for i in range(N):
        if(len(colorlist)>0):
            pencolor(colorlist[i%len(colorlist)])
        forward(L)
        left(angle)
        L += Lplus

def main():
    reset()
    setup(400,400)
    ht()
    speed(0)
    pencolor('#eea2a4')
    n = 40
    i=Screen().numinput("Input", "Sides:", 3, minval=3, maxval=12)
    i=int(i)
    angle = 360/i+0.5
    spiral_line(angle,3,2,i*n)
    
    return "Done!"


if __name__ == "__main__":
    main()
    mainloop()
 