import turtle

t = turtle.Turtle()

t.penup()
t.goto(-300, 0)
t.pendown()

i = 0
while i < 15:
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    i += 1

t.penup()
t.goto(-300, -80)
t.pendown()

i = 0
while i < 10:
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    i += 1

turtle.done()