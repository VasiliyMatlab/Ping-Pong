import turtle

#                              Поле:
#                          LENGTH = 1000
#   |<--------------------------------------------------------->|
#   .___________________________________________________________.--
#   |                            0|                             | ^
#   |       ROCKET_IDENT         1                              | |
#   |----|<--------------        2|                             | |
#   |  .___.--                   3                       .___.  | |
#   |  |   | ^                   4|                      |   |  | |
#   |  |   | |                   .                       |   |  | |
#   |  |   | | ROCKET_WIDTH      .|                      |   |  | | WIDTH = 600
#   |  |   | |                   .                       |   |  | |
#   |  |   | v                  20|                      |   |  | |
#   |  '~~~'--                  21                       '~~~'  | |
#   |  |   | ROCKET_LENGTH      22|                             | |
#   |  |<->|---------------     23                              | |
#   |                           24|                             | v
#   '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'--
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

# Параметры ракеток
ROCKET_IDENT  = 50  # отступ ракетки от края поля
ROCKET_LENGTH = 10  # длина ракетки
ROCKET_WIDTH  = 100 # ширина ракетки
PIX_PER_VALUE = 10  # кол-во пикслей в единице длины
VELOCITY      = 10  # скорость перемещения ракетки
if ROCKET_IDENT < (ROCKET_LENGTH / 2):
    ROCKET_IDENT = ROCKET_LENGTH / 2

# Создание левой ракетки
rocket_left = turtle.Turtle()
rocket_left.color("white")
rocket_left.shape("square")
rocket_left.shapesize(stretch_len = ROCKET_LENGTH/PIX_PER_VALUE/2, \
    stretch_wid = ROCKET_WIDTH/PIX_PER_VALUE/2)
rocket_left.penup()
rocket_left.goto(-LENGTH/2 + ROCKET_IDENT, 0)

# Создание правой ракетки
rocket_right = turtle.Turtle()
rocket_right.color("white")
rocket_right.shape("square")
rocket_right.shapesize(stretch_len = ROCKET_LENGTH/PIX_PER_VALUE/2, \
    stretch_wid = ROCKET_WIDTH/PIX_PER_VALUE/2)
rocket_right.penup()
rocket_right.goto(LENGTH/2 - ROCKET_IDENT, 0)

# Движение левой ракетки вверх
def left_move_up():
    y = rocket_left.ycor() + VELOCITY
    if y > (WIDTH/2 - ROCKET_WIDTH/2):
        y = WIDTH/2 - ROCKET_WIDTH/2
    rocket_left.sety(y)

# Движение левой ракетки вниз
def left_move_down():
    y = rocket_left.ycor() - VELOCITY
    if y < (-WIDTH/2 + ROCKET_WIDTH/2):
        y = -WIDTH/2 + ROCKET_WIDTH/2
    rocket_left.sety(y)

# Движение правой ракетки вверх
def right_move_up():
    y = rocket_right.ycor() + VELOCITY
    if y > (WIDTH/2 - ROCKET_WIDTH/2):
        y = WIDTH/2 - ROCKET_WIDTH/2
    rocket_right.sety(y)

# Движение правой ракетки вниз
def right_move_down():
    y = rocket_right.ycor() - VELOCITY
    if y < (-WIDTH/2 + ROCKET_WIDTH/2):
        y = -WIDTH/2 + ROCKET_WIDTH/2
    rocket_right.sety(y)

window.listen()
window.onkeypress(left_move_up, 'w')
window.onkeypress(left_move_down, 's')
window.onkeypress(right_move_up, 'Up')
window.onkeypress(right_move_down, 'Down')

window.mainloop()