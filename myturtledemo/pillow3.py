from turtle import *

def main():
    reset()
    W = 600
    H = 600
    setup(W,H)
    speed(0)
    #colors = ['#c6e6e8','#ed556a'] #['海天蓝','山茶红']
    colors1 = ['#b89485','#fc6315']
    colors2 = ['#f8f4ed','#ebb10d']
    colors3 = ['#66462a','#b89485']
    pencolor('white')
    L=150
    angle=120
    N1 = int((W/L+2)/2)*2
    N2 = int(H/L)+2
    penup()
    goto(-W/2-L,-H/2-L)
    xy = position()    
    for i in range(N2):
        penup()
        forward(L)
        left(angle)
        forward(L)
        right(angle)
        if i%2==1:
            backward(L)
        xy=position()  

        seth(0)
        pendown()
        
        for j in range(N1):
            if i%2==0:
                cl = colors1[j%len(colors1)]
            else:
                cl = colors2[j%len(colors2)]
            pencolor(cl)
            fillcolor(cl)
            begin_fill()
            forward(L)
            left(angle)
            forward(L)
            right(angle)
            forward(L)
            right(angle)
            forward(L)
            left(angle)
            end_fill() 
           
        for j in range(N1):
            if i%2==0:
                cl = colors2[j%len(colors2)]
            else:
                cl = colors3[j%len(colors3)]
                
            pencolor(cl)
            fillcolor(cl)
            begin_fill()
            left(angle)
            forward(L)
            left(angle)
            forward(L)
            left(angle)
            forward(L)
            backward(L)
        
            end_fill() 
   
    ht()
    

    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()