from turtle import *

def draw_square_at(x, y):
    penup()        
    goto(x, y)      
    pendown()     
    for _ in range(4):
        forward(100)   
        right(90)     

    done()
# ფუნქციის გამოძახება:
# მაგ., (50, 50)-ზე კვადრატის დახატვა
# draw_square_at(50, 50)

exitonclick()