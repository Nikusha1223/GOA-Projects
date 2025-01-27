from turtle import * 

#we want to paint a house 

#step 1: draw a square 
speed(30)
width(7) 
color("green")
forward(200)
left(90) 


forward(200) 
left(90) 


forward(200) 
left(90) 


forward(200) 
left(90) 
#end of squre

#drawing a door

forward(70)  
color("yellow")
begin_fill()
left(90) 
forward(120)
 
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown() 


color("red") 
begin_fill() 
right (150) 
forward(200)
left(120)
forward(200)
end_fill() 

#next step paint a window 
penup() 
pendown
color("brown")
begin_fill() 

left(30)
forward(120) 
penup()
pendown() 

left(90)
forward(55)

left(90)
forward(45)

left(90) 
forward(55) 
end_fill()

penup()
pendown

left(90) 
color("brown")
penup()
pendown()
forward(45)

penup()
pendown
goto(0, 0)

left(90)
forward(70)
color("yellow")
penup()
pendown()
forward(60) 

penup()
pendown
goto(200,200)
color("brown")
begin_fill()
right(90)
forward(80)

penup()
pendown()

right(90) 
forward(55)

left(90)
forward(45)

left(90)
forward(55)
penup()
pendown

left(90)
penup()
pendown()
forward(45)
end_fill() 



exitonclick()