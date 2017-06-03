import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()
    i = 1
    while i < 9:
        brad.color("blue")
        brad.forward(100)
        i = i + 1
        brad.right(60)
    
    window.exitonclick()

draw_square()
