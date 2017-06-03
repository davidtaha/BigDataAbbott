import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()
    i = 1
    brad.color("blue")
    while i < 9:
        brad.forward(100)
        i = i + 1
        brad.right(45)
    
    window.exitonclick()

draw_square()
