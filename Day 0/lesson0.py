from turtle import *



# we mant to paint the house
width (7)
# step 1: draw a square
color ("red")

forward (200)
left (90)


forward (200)
left (90)


forward (200)
left (90)

#end of square
#drawing a door
begin_fill()
forward(200)
left(90)
forward(70)
color("black")
left(90)
forward(100)
right(90)
forward(65)
right(90)
forward(100)


penup()
goto(200, 200)
pendown()
left(210)

#drawing a roof

color("yellow")
begin_fill()
forward(176)
left(114)
forward(190)
end_fill()



exitonclick ()