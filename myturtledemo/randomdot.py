from turtle import *
import random


def paint_frame(L = [200,200]):
    penup()
    goto(-L[0]/2,-L[1]/2)
    seth(0)
    pendown()
    for i in range(2):
        fd(L[0])
        left(90)
        fd(L[1])
        left(90)
        
def main():
    
    reset()
    bgcolor("#eea2a4")
    setup(400,400)
    
    speed(0)
    color0 = '#eea2a4'
    color1 = 'white'
    
    fillcolor(color0)
    pencolor(color1)
    begin_fill()
    paint_frame([400,400])
    end_fill()
    
    pensize(2)
    colormode(255)
    
    ht()
    
    for i in range(20):
	    rcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	    pencolor(rcolor)
	    fillcolor(rcolor)
	    #pencolor(255,255,255)
	    rdot = random.randint(9,30)
	    dotpos = [random.randint(-190,190),random.randint(-190,190)]
	    #penup()
	    goto(dotpos)
	    seth(random.randint(0,360))
	    #pendown()
	    #dot(rdot)
	    n = random.randint(3,9)
	    begin_fill()
	    circle(rdot,steps=n)
	    end_fill()
        
    
    return "Done"

if __name__ == "__main__":
    main()
    mainloop()