import turtle

#            Поле:
#        LENGTH = 1000
#   |<------------------->|
#   ._____________________.--
#   |         0|          | ^
#   |         1           | |
#   |         2|          | | WIDTH = 600
#   |         .           | |
#   |        24|          | v
#   '~~~~~~~~~~~~~~~~~~~~~'--
#

# Размеры поля
LENGTH = 1000
WIDTH  = 600

# Параметры окна
window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=1.0, height=0.99)
window.bgcolor("black")

# Отрисовка задней части поля
border = turtle.Turtle()
border.speed(0)
border.hideturtle()
border.color('green')
border.begin_fill()
border.goto(-LENGTH/2, WIDTH/2)
border.goto(LENGTH/2, WIDTH/2)
border.goto(LENGTH/2, -WIDTH/2)
border.goto(-LENGTH/2, -WIDTH/2)
border.goto(-LENGTH/2, WIDTH/2)
border.end_fill()

# Отрисовка пунктирной линии в центре
NUM_GRID  = 25               # кол-во пунктирных отрезков
GRID_STEP = WIDTH / NUM_GRID # длина пунктира
border.goto(0, WIDTH/2)
border.color("white")
border.setheading(270)
for i in range(NUM_GRID):
    if not i % 2:
        border.forward(GRID_STEP)
    else:
        border.up()
        border.forward(GRID_STEP)
        border.down()

window.mainloop()