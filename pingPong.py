import turtle
from random import choice, randint

#
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
window.tracer(1.5)

# Отрисовка задней части поля
border = turtle.Turtle(visible=False)
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-LENGTH/2, WIDTH/2)
border.goto(LENGTH/2, WIDTH/2)
border.goto(LENGTH/2, -WIDTH/2)
border.goto(-LENGTH/2, -WIDTH/2)
border.goto(-LENGTH/2, WIDTH/2)
border.end_fill()

# Отрисовка пунктирных линий в центре
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
rocket_left.speed(0)
rocket_left.color("white")
rocket_left.shape("square")
rocket_left.shapesize(stretch_len = ROCKET_LENGTH/PIX_PER_VALUE/2, \
    stretch_wid = ROCKET_WIDTH/PIX_PER_VALUE/2)
rocket_left.penup()
rocket_left.goto(-LENGTH/2 + ROCKET_IDENT, 0)

# Создание правой ракетки
rocket_right = turtle.Turtle()
rocket_right.speed(0)
rocket_right.color("white")
rocket_right.shape("square")
rocket_right.shapesize(stretch_len = ROCKET_LENGTH/2/PIX_PER_VALUE, \
    stretch_wid = ROCKET_WIDTH/2/PIX_PER_VALUE)
rocket_right.penup()
rocket_right.goto(LENGTH/2 - ROCKET_IDENT, 0)

# Создание мячика
DIAMETER = 20 # диаметр мячика
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(DIAMETER/2/PIX_PER_VALUE)
ball.color("red")
ball.penup()
ball.dx = choice([-4,-3,-2, 2,3,4]) # ск-ть перемещения мячика по x
ball.dy = choice([-4,-3,-2, 2,3,4]) # ск-ть перемещения мячика по y

# Счет игроков
FONT = ("Arial", 44) # шрифт
# Левый игрок
score_left  = 0
Point_left  = turtle.Turtle(visible=False)
Point_left.color("white")
Point_left.penup()
Point_left.setposition(-LENGTH/5, WIDTH/2)
Point_left.write(score_left, font=FONT)
# Правый игрок
score_right = 0
Point_right = turtle.Turtle(visible=False)
Point_right.color("white")
Point_right.penup()
Point_right.setposition(LENGTH/5, WIDTH/2)
Point_right.write(score_right, font=FONT)

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

while True:
    window.update()
    
    # Перемещение мячика
    try:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
    except Exception:
        print("Game has been aborted")
        exit()
    
    # Отражение от верхней и нижней стенок
    if ball.ycor() >= (WIDTH/2 - DIAMETER/2):
        ball.dy = -ball.dy
    elif ball.ycor() <= (-WIDTH/2 + DIAMETER/2):
        ball.dy = -ball.dy
    
    # Если мячик в левой половине
    if ball.xcor() < 0:   
        # Отражение от лицевой стороны левой ракетки
        if (ball.ycor() >= rocket_left.ycor()-ROCKET_WIDTH/2) and \
                (ball.ycor() <= rocket_left.ycor()+ROCKET_WIDTH/2) and \
                (ball.xcor() <= rocket_left.xcor()+ROCKET_LENGTH/2+DIAMETER/2):
            ball.dx = -ball.dx
        # Достижение левой стенки
        if ball.xcor() <= (-LENGTH/2 + DIAMETER/2):
            ball.dx = choice([-4,-3,-2, 2,3,4])
            ball.dy = choice([-4,-3,-2, 2,3,4])
            score_right += 1
            Point_right.clear()
            Point_right.write(score_right, font=FONT)
            if score_right == 7:
                ball.goto(0, 0)
                print("Player B win")
                print("Gameover")
                break
            ball.goto(0, randint(-WIDTH/4, WIDTH/4))
    # Если мячик в правой половине
    else:
        # Отражение от лицевой стороны правой ракетки
        if (ball.ycor() >= rocket_right.ycor()-ROCKET_WIDTH/2) and \
                (ball.ycor() <= rocket_right.ycor()+ROCKET_WIDTH/2) and \
                (ball.xcor() >= rocket_right.xcor()-\
                ROCKET_LENGTH/2-DIAMETER/2):
                ball.dx = -ball.dx
        # Достижение правой стенки
        if ball.xcor() >= (LENGTH/2 - DIAMETER/2):
            ball.dx = choice([-4,-3,-2, 2,3,4])
            ball.dy = choice([-4,-3,-2, 2,3,4])
            score_left += 1
            Point_left.clear()
            Point_left.write(score_left, font=FONT)
            if score_left == 7:
                ball.goto(0, 0)
                print("Player A win")
                print("Gameover")
                break
            ball.goto(0, randint(-WIDTH/4, WIDTH/4))

turtle.mainloop()