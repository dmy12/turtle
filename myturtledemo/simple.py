
import turtle

def circle1():
    tt = turtle.Turtle()
    tt.hideturtle()
    tt.pencolor('white')
    tt.fillcolor('pink')
    tt.speed(0)
    n=17
    angle=360/n
    length=50
    tt.begin_fill()
    for i in range(n):
        tt.circle(length)
        tt.right(angle)
    tt.end_fill()
    
    

def flower1():
    radius = 20
    LL = 40
    n=17
    angle = 30

    tt = turtle.Turtle()
    tt.speed(0.1)
    tt.pensize(0.1)
    tt.pencolor('orange')
    tt.circle(radius)
    tt.pencolor('orange')
    tt.fillcolor('yellow')
    
    for i in range(n):
        tt.penup()
        tt.circle(radius,extent=360/n)
        tt.pendown()
        tt.begin_fill()
        tt.right(90+angle/2)
        tt.fd(LL)
        tt.left(angle)
        tt.fd(LL)
        tt.left(180-angle)
        tt.fd(LL)
        tt.left(angle)
        tt.fd(LL)
        tt.rt(90+angle/2)
        tt.end_fill()
        
    tt.hideturtle()
            


def flower2():    

    tt = turtle.Turtle()
    tt.speed(0)
    tt.pensize(1)
    
    tt.pencolor('green')
    tt.fillcolor('yellow')
    
    for i in range(12):
        tt.penup()
        tt.circle(75,extent=30)
        tt.pendown()
        tt.begin_fill()
        tt.right(105)
        tt.fd(60)
        tt.left(30)
        tt.fd(60)
        tt.left(150)
        tt.fd(60)
        tt.left(30)
        tt.fd(60)
        tt.left(75)
        tt.end_fill()
    
    tt.ht()
    
        
    

    
def main():

    turtle.setup(400,400)
    
    turtle.hideturtle()
    
    circle1()
    
    return 'Done'

if __name__ == "__main__":
    
    main()
    mainloop()
    
 