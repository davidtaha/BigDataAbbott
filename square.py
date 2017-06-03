import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    i = 1
    while i < 5:
        brad.forward(100)
        brad.right(90)
        i = i + 1
    
    window.exitonclick()

draw_square()
