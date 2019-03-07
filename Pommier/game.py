import turtle
import winsound
import random

rand = random.randint(-290, 290)
life = 3
score = 0

#Fenêtre
window = turtle.Screen()
window.title("Pommier - Projet Python")
window.bgcolor("#5ab6dd")
window.setup(width=800, height=600)
window.tracer(30)

#Fond Herbe
back4 = turtle.Turtle()
back4.shape("circle")
back4.color("#394c01")
back4.shapesize(stretch_wid=23, stretch_len=23)
back4.penup()
back4.goto(200, 300)
back5 = turtle.Turtle()
back5.shape("circle")
back5.color("#394c01")
back5.shapesize(stretch_wid=23, stretch_len=23)
back5.penup()
back5.goto(-200, 300)

back1 = turtle.Turtle()
back1.shape("circle")
back1.color("#476e30")
back1.shapesize(stretch_wid=23, stretch_len=23)
back1.penup()
back1.goto(130, -250)
back1 = turtle.Turtle()
back1.shape("circle")
back1.color("#476e30")
back1.shapesize(stretch_wid=23, stretch_len=23)
back1.penup()
back1.goto(-190, -270)
back2 = turtle.Turtle()
back2.shape("circle")
back2.color("#478d30")
back2.shapesize(stretch_wid=20, stretch_len=20)
back2.penup()
back2.goto(250, -250)
back3 = turtle.Turtle()
back3.shape("circle")
back3.color("#478d30")
back3.shapesize(stretch_wid=20, stretch_len=20)
back3.penup()
back3.goto(-250, -300)

#tronc
tronc = turtle.Turtle()
tronc.shape("square")
tronc.color("#5c4101")
tronc.shapesize(stretch_wid=20, stretch_len=12)
tronc.penup()
tronc.goto(0, 0)

#Feuilles
leaf = turtle.Turtle()
leaf.shape("circle")
leaf.color("#476e30")
leaf.shapesize(stretch_wid=26, stretch_len=26)
leaf.penup()
leaf.goto(350, 400)
leaf4 = turtle.Turtle()
leaf4.shape("circle")
leaf4.color("#476e30")
leaf4.shapesize(stretch_wid=26, stretch_len=26)
leaf4.penup()
leaf4.goto(-350, 400)
leaf2 = turtle.Turtle()
leaf2.shape("circle")
leaf2.color("#478d30")
leaf2.shapesize(stretch_wid=26, stretch_len=26)
leaf2.penup()
leaf2.goto(130, 400)
leaf3 = turtle.Turtle()
leaf3.shape("circle")
leaf3.color("#478d30")
leaf3.shapesize(stretch_wid=26, stretch_len=26)
leaf3.penup()
leaf3.goto(-130, 400)

#Sol
ground = turtle.Turtle()
ground.shape("square")
ground.color("#604325")
ground.shapesize(stretch_wid=6, stretch_len=300)
ground.penup()
ground.goto(0, -280)

#Herbe
ground = turtle.Turtle()
ground.shape("square")
ground.color("#60a925")
ground.shapesize(stretch_wid=1, stretch_len=300)
ground.penup()
ground.goto(0, -210)

#Pommes
apple = turtle.Turtle()
apple.shape("circle")
apple.color("#8c0004")
apple.shapesize(stretch_wid=2, stretch_len=2)
apple.penup()
apple.goto(-80,260)
apple = turtle.Turtle()
apple.shape("circle")
apple.color("#8c0004")
apple.shapesize(stretch_wid=2, stretch_len=2)
apple.penup()
apple.goto(-220,220)
apple = turtle.Turtle()
apple.shape("circle")
apple.color("#8c0004")
apple.shapesize(stretch_wid=2, stretch_len=2)
apple.penup()
apple.goto(120,230)
apple = turtle.Turtle()
apple.shape("circle")
apple.color("#8c0004")
apple.shapesize(stretch_wid=2, stretch_len=2)
apple.penup()
apple.goto(250,250)

#panier
player = turtle.Turtle()
player.shape("square")
player.color("#fba201")
player.speed(0)
player.shapesize(stretch_wid=1, stretch_len=4.5)
player.penup()
player.goto(0, -180)

#Balle
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(rand, 290)
# Vitesse de déplacement de la balle selon l'axe
ball.dy = -3

#Pen - Vies
penLife = turtle.Turtle()
penLife.speed(0)
penLife.color("white")
penLife.penup()
penLife.hideturtle()
penLife.goto(250,0)
penLife.write("{} vies restantes".format(life), align="center", font=("Courier", 14, "normal"))

#Pen - Score
penScore = turtle.Turtle()
penScore.speed(0)
penScore.color("white")
penScore.penup()
penScore.hideturtle()
penScore.goto(-250, 0)
penScore.write("Aucune Pomme", align="center", font=("Courier", 14, "normal"))

#Déplacements
def player_right():
    x = player.xcor()
    x += 55
    player.setx(x)

def player_left():
    x = player.xcor()
    x -= 55
    player.setx(x)

#Configuration des touches
window.listen()
window.onkeypress(player_right, "Right")
window.onkeypress(player_left, "Left")
window.onkeypress(player_right, "d")
window.onkeypress(player_left, "q")

while True:
    window.update()

    # Déplacements de la balle
    ball.sety(ball.ycor() + ball.dy)

    #Collision sol
    if ball.ycor() < -210:
        penLife.clear()
        life -= 1
        if life >= 0:
            penLife.write("vies restantes : {}".format(life), align="center", font=("Courier", 14, "normal"))
            ball.goto(random.randint(-300, 300), 290)
        elif life < 0:
            ball.dy = 0
            ball.goto(0, 0)
            penLife.write("Partie terminée".format(life), align="center", font=("Courier", 14, "normal"))


    # Panier
    if (ball.ycor() < -160 and ball.ycor() > -170) and (ball.xcor() < player.xcor() + 70 and ball.xcor() > player.xcor() - 70):
        ball.goto(random.randint(-300, 300), 290)
        score += 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        penScore.clear()
        penScore.write("Score : {}".format(score), align="center", font=("Courier", 14, "normal"))
