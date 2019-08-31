import turtle

pen = turtle.Pen()
pen.color('darkred')
pen.width(7)

for i in range(100):
    pen.forward(100 - i)
    pen.left(60)

turtle.done()


