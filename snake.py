import random
import turtle as t

t.bgcolor("yellow")

snake = t.Turtle()
snake.shape("square")
snake.color("red")
snake.speed(0)
snake.penup()
snake.hideturtle()

blad = t.Turtle()
blad_form = ((0, 0), (14, 2), (18, 6), (20, 20), \
            (6, 18), (2, 14))
t.register_shape("blad", blad_form)
blad.shape("blad")
blad.color("green")
blad.penup()
blad.hideturtle()
blad.speed(0)

spel_startat = False
textsköldpadda = t.Turtle()
textsköldpadda.write("Press( Enter ) to start the game", \
                     align="center", font=("Arial", 16, 'bold'))
textsköldpadda.hideturtle()

poängsköldpadda = t.Turtle()
poängsköldpadda.hideturtle()
poängsköldpadda.speed(0)

def utanför_fönster():
    vänster_vägg = -t.window_width() / 2
    höger_vägg = t.window_width() / 2
    övre_vägg = t.window_height() / 2
    nedre_vägg = -t.window_height() / 2
    (x, y) = snake.pos()
    utanför = \
            x< vänster_vägg or \
            x> höger_vägg or \
            y< nedre_vägg or \
            y> övre_vägg
    return utanför

def spel_slut():
    snake.color("yellow")
    blad.color("yellow")
    t.penup()
    t.hideturtle()
    t.write("THE GAME IS OVER!", align="center", font=("Arial", 30, "normal"))

def visa_poäng(aktuell_poäng):
    poängsköldpadda.clear()
    poängsköldpadda.penup()
    x = (t.window_width() / 2) -50
    y = (t.window_height() /2) - 50
    poängsköldpadda.setpos(x, y)
    poängsköldpadda.write(str(aktuell_poäng), align="right", \
                         font=("Arial", 40, "bold"))

def placera_blad():
    blad.ht()
    blad.setx(random.randint(-200, 200))
    blad.sety(random.randint(-200, 200))
    blad.st()

def starta_spel():
    global spel_startat
    if spel_startat:
        return
    spel_startat = True

    poäng = 0
    textsköldpadda.clear()

    snake_hastighet = 2
    snake_längd = 3
    snake.shapesize(1, snake_längd, 1)
    snake.showturtle()
    visa_poäng(poäng)
    placera_blad()

    while True:
        snake.forward(snake_hastighet)
        if snake.distance(blad)< 20:
            placera_blad()
            snake_längd = snake_längd + 1
            snake.shapesize(1, snake_längd, 1)
            snake_hastighet = snake_hastighet + 1
            poäng = poäng + 10
            visa_poäng(poäng)
        if utanför_fönster():
            spel_slut()
            break
def flytta_uppåt():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)


def flytta_nedåt():
    if snake.heading() == 0 or snake.heading() ==180:
        snake.setheading(270)

def flytta_vänster():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def flytta_höger():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)

t.onkey(starta_spel, "space")
t.onkey(flytta_uppåt, "Up")
t.onkey(flytta_höger, "Right")
t.onkey(flytta_nedåt, "Down")
t.onkey(flytta_vänster,"Left")

t.onkey(flytta_uppåt, "w")
t.onkey(flytta_höger, "d")
t.onkey(flytta_nedåt, "s")
t.onkey(flytta_vänster,"a")

t.listen()
t.mainloop()
