from turtle import *


#we want to paint a house

#step 1: drae a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

#end of squarl

#drawing a door


forward(70)
begin_fill()
color("yellow")
left(90)

forward(120)   #Height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of roof

#drawing a windows

left(30)
begin_fill()
color("brown")
forward(60)
left(90)
forward(50)
left(90)
forward(55)
left(90)
forward(50)
end_fill()

penup()
goto(200,200)
pendown()

forward(50)
begin_fill()
left(90)
forward(55)
left(90)
forward(50)
left(90)
forward(50)
end_fill()









exitonclick()



