# Frieze Pattern, Simple lines

from turtle import *
import time

def Frieze_Group_Example(isymmetry=0):
    IUC = ""
    penup()
    backward(300)
    pendown()
    n=10
    shift = 60
    fsize = 40
    if isymmetry==0:
        IUC = 'p1, hop'
        for i in range(n):
            forward(shift)
            left(120)
            forward(fsize)
            backward(fsize)
            right(120)
    elif isymmetry==1:
        IUC = 'p11g, step'
        for i in range(int(n/2)):
            forward(shift)
            left(120)
            forward(fsize)
            backward(fsize)
            right(120)
            forward(shift)
            right(120)
            forward(fsize)
            backward(fsize)
            left(120)
    elif isymmetry==2:
        IUC = 'p1m1, sidle'
        for i in range(n):
            forward(shift)
            left(90)
            forward(fsize)
            backward(fsize)
            right(90)
    elif isymmetry==3:
        IUC = 'p2, spinning hop'
        for i in range(n):
            forward(shift)
            left(120)
            forward(fsize)
            backward(fsize)
            right(180)
            forward(fsize)
            backward(fsize)
            left(60)
    elif isymmetry==4:
        IUC = 'p2mg, spinning sidle'
        angle0=50
        angles=[angle0, 2*angle0]
        for i in range(n):
            forward(shift)
            left(angles[0])
            forward(fsize)
            right(angles[1])
            forward(fsize)
            left(angles[0])
            forward(shift)
            right(angles[0])
            forward(fsize)
            left(angles[1])
            forward(fsize)
            right(angles[0])
    elif isymmetry==5:
        IUC = 'p11m, jump'
        for i in range(n):
            forward(shift)
            left(120)
            forward(fsize)
            backward(fsize)
            right(120)
            right(120)
            forward(fsize)
            backward(fsize)
            left(120)
    elif isymmetry==6:
        IUC = 'p2mm, spinning jump'
        for i in range(n):
            forward(shift)
            left(90)
            forward(fsize)
            backward(fsize)
            right(90)
            right(90)
            forward(fsize)
            backward(fsize)
            left(90)

    return IUC

def show_text(text, line=0):
    line = 20 * line
    goto(0,-250 - line)
    write(text, align="center", font=("Courier", 16, "bold"))

def main():
    W, H = 600, 300
    setup(W,H)
    pensize(10)
    speed(0)
    pencolor('purple')
    #i = input("Enter your value: ")

    i=Screen().numinput("Frieze Group", "Index:", 0, minval=0, maxval=6)
    IUC=Frieze_Group_Example(i)
    
    up()
    
    show_text(IUC)
    
    ht()


    return "Done!"


if __name__ == "__main__":
    main()
    time.sleep(10)
    bye()