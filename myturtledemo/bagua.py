
from turtle import *

def gua_frame(radius=300, centerpoint = (0,0)):
    penup()
    goto(centerpoint)
    setheading(270-22.5)
    forward(radius)
    pendown()
    left(90)
    circle(radius,steps=8)

def num2gua(x=0):
    gua = ['0','0','0']
    y = list(bin(x))
    j=0
    for i in range(len(y),2,-1):
        gua[2-j] = y[i-1]
        j += 1
    return gua

def yin(L=60):
    penup()
    backward(L/2.)
    pendown()
    forward(L/3.)
    penup()
    forward(L/3.)
    pendown()
    forward(L/3.)
    penup()
    backward(L/2.)
    pendown()
    
def yang(L=60):
    penup()
    backward(L/2.)
    pendown()
    forward(L)
    penup()
    backward(L/2.)
    pendown()

def yao(yinyang='0',L=60):
    pensize(10)
    if yinyang=='0':
        yin(L)
    else:
        yang(L)
        
def draw_gua(x=0,
             xheading=270, 
             radius=200, 
             spacing=20,
             centerpoint=(0,0)):
    
    gua = num2gua(x)
    penup()
    goto((0,0))
    seth(xheading)
    fd(radius)
    pendown()
    for i in range(3):
        left(90)
        yao(gua[i])
        penup()
        seth(xheading)
        fd(spacing)
        
def bagua(radius=200, spacing=20):
    #[坤艮坎巽震离兑乾]
    for i in range(4):
        draw_gua(i,270+45*i, radius, spacing)
    for i in range(4,8):
        draw_gua(i,45-45*i,radius, spacing)
        
def taiji_half(radius=200,color1="black", color2="white"):
    fillcolor(color1)
    begin_fill()
    circle(radius/2,180)
    circle(radius,180)
    circle(radius/2,-180)
    end_fill()
    penup()
    right(90)
    fd(0.35*radius)
    left(90)
    pendown()
    fillcolor(color2)
    begin_fill()
    circle(-radius*0.15)
    end_fill()
    penup()
    left(90)
    fd(0.35*radius)
    right(90)
    pendown()    
    
def taiji(radius=200, xheading = 0, centerpoint=(0,0)):
    penup()
    goto(centerpoint)
    seth(xheading)
    pendown()
    color1, color2 = "black", "white"
    taiji_half(radius,color1,color2)
    taiji_half(radius,color2,color1)


    
def main():
    reset()
    speed(0)
    shape("turtle")
    
    #frame
    gua_frame(220)
    gua_frame(240)
    
    speed(0.5)
    bagua(140)
    
    speed(0.8)
    pensize(2)
    taiji(100,180)
    
    ht()
    
    return "八卦"

if __name__ == '__main__':
    main()
    mainloop()