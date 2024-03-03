import turtle
s=turtle.getscreen()
y=turtle.Turtle()
y.shape('turtle')
y.color('blue')
y.speed()
y.begin_fill()
y.fillcolor('orange')
# Draw a square with 200 px 
for a in range(4):
    y.forward(200)
    y.right(90)
    y.forward(200)

# Draw a triangle
for b in range(3):
    y.forward(150)
    y.right(120)
    y.forward(150)


# Draw a circle with radius 50 px
y.circle(50)
y.end_fill()

# Draw a self writing line
for a in range(40):
    y.forward(50+10*a)
    y.right(90)

y.end_fill()
y.hideturtle()
turtle.exitonclick()