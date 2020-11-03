
from turtle import *
import math

def main(L = 10):
    reset()
    setup(400,400)
    ht()
    pencolor('red')
    #fillcolor('white')
    n=120
    speed(0)
    pensize(1)
    penup()
    goto(0,5*L)
    pendown()
    #begin_fill()
    for i in range(1,n+1):
        t = i*math.pi*2/n
        x = L*(16*math.sin(t)**3)
        y = L*(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))
        goto(x,y)
        if t<math.pi:
            goto(-5*L,0)
        else:
            goto(5*L,0)
        
        penup()
        t = t+math.pi/6
        x = L*(16*math.sin(t)**3)
        y = L*(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))
        goto(x,y)
        pendown()
    #end_fill()
    return 'Done'

if __name__ == "__main__":
    main()
    mainloop()
