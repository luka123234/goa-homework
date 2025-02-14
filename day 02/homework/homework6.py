import turtle


screen = turtle.Screen()
screen.bgcolor("white")  


t = turtle.Turtle()


def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()

    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)

    t.end_fill()


def draw_triangle(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()

    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)

    t.end_fill()


draw_rectangle(-100, 0, 200, 150, "gray")
draw_rectangle(-100, 100, 200, 100, "gray")

draw_rectangle(-140, 40, 40, 80, "gray")
draw_rectangle(100, 40, 40, 80, "gray")
draw_rectangle(-140, 120, 40, 80, "gray")
draw_rectangle(100, 120, 40, 80, "gray")
draw_triangle(-140, 120, 40, "red")
draw_triangle(100, 120, 40, "red")


draw_triangle(-100, 100, 200, "darkred")


draw_rectangle(-30, -90, 40, 60, "brown")


draw_rectangle(-80, 50, 20, 20, "black")
draw_rectangle(60, 50, 20, 20, "black")



