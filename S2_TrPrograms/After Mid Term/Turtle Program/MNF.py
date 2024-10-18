import turtle
screen = turtle.Screen()
screen.bgcolor("white")
flag_turtle = turtle.Turtle()
flag_turtle.speed(2)

def draw_rectangle(color, width, height):
    flag_turtle.begin_fill()
    flag_turtle.fillcolor(color)
    for _ in range(2):
        flag_turtle.forward(width)
        flag_turtle.right(90)
        flag_turtle.forward(height)
        flag_turtle.right(90)
    flag_turtle.end_fill()

flag_turtle.goto(0,300)
draw_rectangle("#FFD200", 400, 100) #yellow
flag_turtle.goto(0,200)
draw_rectangle("#34B233", 400, 100) #green
flag_turtle.goto(0,100)
draw_rectangle("#EA2839", 400, 100) #red

#flag_turtle.goto(200,100)
#flag_turtle.right(45)



flag_turtle.goto(0,0)
flag_turtle.right(90)
flag_turtle.fd(100)
flag_turtle.hideturtle()

 
##my_turtle.fd(300)
##my_turtle.left(90)
##my_turtle.fd(100)
##my_turtle.left(90)
##my_turtle.fd(300)
##my_turtle.left(90)
##my_turtle.fd(100)
