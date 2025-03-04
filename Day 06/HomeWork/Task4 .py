from turtle import * 
#painting a tower

#first step draw wall
speed(30) 
width(10) 
color("black") 

begin_fill()

forward(150) 
left(90) 
forward(300) 
left(90) 
forward(150) 
left(90) 
forward(300) 

end_fill() 

#step 2 drawing Door 

goto(0 , 0) 

left(90) 

begin_fill()
forward(50) 
color("brown") 

left(90)
forward(100)
right(90) 
forward(50)
right(90)
forward(100)

end_fill()

goto(50 , 0)

#step 3 paintig a base 
color("black")
penup()
goto(0 ,300 ) 
pendown() 


left(180) 
forward(50) 
right(90) 
forward(150)
right(90)
forward(50)

#step 4 painting a flag 
color("green")
penup()
goto(0, 350) 
pendown()

left(180) 
forward(60) 
left(90) 
forward(50)

begin_fill()
right(90)
forward(50)
right(90) 
forward(50)
right(90)
forward(50)
end_fill()


exitonclick()