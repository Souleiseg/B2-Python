import turtle
import winsound

#Fenêtre
window = turtle.Screen()
window.title("Squash - Projet Python")
window.bgcolor("black")
window.setup(width=600, height=1000)
window.tracer(30)

#Paddle
paddle_player = turtle.Turtle()
paddle_player.speed(0)
paddle_player.shape("square")
paddle_player.color("white")
paddle_player.shapesize(stretch_wid=1, stretch_len=4)
paddle_player.penup()
paddle_player.goto(0, -430)

#Pen - Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,460)
pen.write("Score - 0 rebond", align="center", font=("Courier", 24, "normal"))

#Score
score_player = 0

#interface
interface = turtle.Turtle()
interface.shape("square")
interface.color("blue")
interface.shapesize(stretch_wid=0.5, stretch_len=30)
interface.penup()
interface.goto(0, 450)

#Balle
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 200)
# Vitesse de déplacement de la balle selon l'axe
ball.dx = 1.5
ball.dy = -1.5

#Déplacements
def paddle_player_right():
    x = paddle_player.xcor()
    x += 40
    paddle_player.setx(x)

def paddle_player_left():
    x = paddle_player.xcor()
    x -= 40
    paddle_player.setx(x)

#Configuration des touches
window.listen()
window.onkeypress(paddle_player_right, "Right")
window.onkeypress(paddle_player_left, "Left")
window.onkeypress(paddle_player_right, "d")
window.onkeypress(paddle_player_left, "q")



while True:
    window.update()

    #Déplacements de la balle
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Collisions
    #Haut
    # Collisions avec les bords
    # Haut
    if ball.ycor() > 430:
        ball.sety(430)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        score_player += 10
        if (score_player ==1 ):
            pen.write("Score - {} rebond".format(score_player), align="center", font=("Courier", 24, "normal"))
        elif (score_player > 1 and score_player < 10):
            pen.write("Score - {} rebonds".format(score_player), align="center",font=("Courier", 24, "normal"))
        elif (score_player >= 10 and score_player < 20):
            pen.write("Score - {} rebonds !".format(score_player), align="center",font=("Courier", 24, "normal"))
        elif (score_player >= 20 and score_player < 30):
            pen.write("Score - Waw ! {} rebonds !!".format(score_player), align="center",font=("Courier", 24, "normal"))
        elif (score_player >= 30):
            pen.write("Score -  {} rebonds ?! Trop fort !".format(score_player), align="center",font=("Courier", 20, "normal"))

    #Bas
    if ball.ycor() < -500:
        ball.goto(0, 200)
        paddle_player.goto(0, -430)
        ball.dx *= -1
        score_player = 0
        pen.clear()
        pen.write("Score - {} rebond".format(score_player), align="center", font=("Courier", 24, "normal"))

    #Gauche
    if ball.xcor() < -295:
        ball.setx(-295)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Droite
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Paddle
    if (ball.ycor() < -420 and ball.ycor() > -430) and (ball.xcor() < paddle_player.xcor() + 70 and ball.xcor() > paddle_player.xcor() -70):
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Paddle - côté gauche
    if paddle_player.xcor() > 240:
        paddle_player.setx(240)

    #Paddle - côté droit
    if paddle_player.xcor() < -240:
        paddle_player.setx(-240)



