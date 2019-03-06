# Import du module turtle (similaire à Pygame) - Adapté pour les débutants
import turtle
import winsound
import time

# Création de la fenêtre de jeu
window = turtle.Screen()
window.title("Pong - Projet Python")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(30)

#Score
score_player = 0
score_player2 = 0

# Paddle du joueur
paddle_player = turtle.Turtle()
paddle_player.speed(0)
paddle_player.shape("square")
paddle_player.color("white")
paddle_player.shapesize(stretch_wid=5, stretch_len=1)
paddle_player.penup()
paddle_player.goto(-350, 0)

# Paddle du joueur 2
paddle_player2 = turtle.Turtle()
paddle_player2.speed(0)
paddle_player2.shape("square")
paddle_player2.color("white")
paddle_player2.shapesize(stretch_wid=5, stretch_len=1)
paddle_player2.penup()
paddle_player2.goto(350, 0)

# Balle
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 200)
# Vitesse de déplacement de la balle selon l'axe
ball.dx = 0.1
ball.dy = 0.1

# Pen - Système de score
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Joueur 1: 0   Joueur 2: 0", align="center", font=("Courier", 24, "normal"))

# Fonctions du jeu
def paddle_player_up():
    y = paddle_player.ycor()
    y += 60
    paddle_player.sety(y)

def paddle_player_down():
    y = paddle_player.ycor()
    y -= 60
    paddle_player.sety(y)

def paddle_player2_up():
    y = paddle_player2.ycor()
    y += 60
    paddle_player2.sety(y)

def paddle_player2_down():
    y = paddle_player2.ycor()
    y -= 60
    paddle_player2.sety(y)

# Configuration des touches
window.listen()
window.onkeypress(paddle_player_up, "z")
window.onkeypress(paddle_player_down, "s")

window.onkeypress(paddle_player2_up, "Up")
window.onkeypress(paddle_player2_down, "Down")

# Boucle principale du jeu
while True:

    # Déplacements de la balle
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collisions avec les bords
    # Haut
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Bas
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Droite
    if ball.xcor() > 390:
        ball.goto(0, -200)
        paddle_player.goto(-350, 0)
        ball.dx *= -1
        score_player += 1
        pen.clear()
        pen.write("Joueur 1: {}   Joueur 2: {}".format(score_player, score_player2), align="center", font=("Courier", 24, "normal"))

    # Gauche
    if ball.xcor() < -390:
        ball.goto(0, 200)
        paddle_player2.goto(350, 0)
        ball.dx *= -1
        score_player2 += 1
        pen.clear()
        pen.write("Joueur 1: {}   Joueur 2: {}".format(score_player, score_player2), align="center", font=("Courier", 24, "normal"))


    # Paddle Droite
    # Collision Haut
    if paddle_player2.ycor() > 250:
        paddle_player2.sety(250)

    # Collision Bas
    if paddle_player2.ycor() < -250:
        paddle_player2.sety(-250)

    # Paddle Gauche
    # Collision Haut
    if paddle_player.ycor() > 250:
        paddle_player.sety(250)

    # Collision Bas
    if paddle_player.ycor() < -250:
        paddle_player.sety(-250)

    # Collision balle
    # Paddle Droite
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_player2.ycor() + 50 and ball.ycor() > paddle_player2.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Paddle Gauche
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_player.ycor() + 50 and ball.ycor() > paddle_player.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (score_player == 10 or score_player2 == 10):
        ball.dx = 0
        ball.dy = 0
        pen.clear()
        pen.write("Score final : {}  -  {}".format(score_player, score_player2), align="center", font=("Courier", 24, "normal"))
        time.sleep(5)
        window._destroy()









