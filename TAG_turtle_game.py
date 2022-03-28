import turtle 
import random 
import tkinter 
import tkinter.simpledialog as SD
import tkinter.messagebox as MB


MB.showinfo("CONTROLS", "RED: W,A,S,D \n BLUE: I,J,K,L \n RAGEQUIT: Q")

speed = 20
xboundry = 650
yboundry = 300
timelimit = 45
proximity = 20

while True:  
    option = SD.askstring("GAME OPTION","would you like to do rounds? N/Y")
    option = option.upper()
    if option == 'Y':
        rounds = True
        break
    if option ==    'N':
        rounds = False
        break


game = turtle.Screen()
game.setup(width=xboundry*2,height=yboundry*2)
game.bgcolor("green")

decider = random.randint(1,2)
if decider == 1:
    it = 'red'
elif decider == 2:
    it = 'blue'

tag = turtle.Turtle()
tag.color("grey")
tag.shape("arrow")
tag.penup()

p1 = turtle.Turtle()
p1.penup()
p1.shape("square")
p1.color("blue")
p1.shapesize()
p1.speed(0)
p1.goto(601,-300)
p1.left(180)
p1.direction = "stop"

p2 = turtle.Turtle()
p2.penup() 
p2.shape("square")
p2.color("red")
p2.speed(0)
p2.goto(-601,300)
p2.direction = "stop"


counter = 0
counter2 = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def timer(counter,counter2):
    if counter2 == 10:
        pen.clear()
        pen.write(counter/50, align="center", font=("Courier", 24, "normal"))
        return 1
    else:
        sum = counter2 + 1
        return sum

def exit():
    turtle.bye()

def reset():
    p1.goto(601,-300)
    p2.goto(-601,300)
    if it == 'blue':
        makeblueit()
        p1.direction = "stop"
        p2.direction = "stop"
    if it == 'red':
        makeredit()
        p2.direction = "stop"
        p1.direction = "stop"

def makeblueit():
    arrowx = p1.xcor()
    arrowy = p1.ycor()
    game.tracer(0)
    tag.goto(arrowx - 40, arrowy)
    game.tracer(1)

def makeredit():
    arrowx = p2.xcor()
    arrowy = p2.ycor()
    game.tracer(0)
    tag.goto(arrowx - 40, arrowy)
    game.tracer(1)

def p1stop():
    p1.direction = "stop"

def p2stop():
    p2.direction = "stop"

def p1up():
    p1.direction = "up"

def p1down():
    p1.direction = "down"

def p1left():
    p1.direction = "left"

def p1right():
    p1.direction = "right"



def p2up():
    p2.direction = "up"

def p2down():
    p2.direction = "down"

def p2left():
    p2.direction = "left"

def p2right():
    p2.direction = "right"

def move():
    if p1.direction == "up":
        y = p1.ycor()
        p1.sety(y + speed)

    if p1.direction == "down":
        y = p1.ycor()
        p1.sety(y - speed)

    if p1.direction == "left":
        x = p1.xcor()
        p1.setx(x - speed)

    if p1.direction == "right":
        x = p1.xcor()
        p1.setx(x + speed)

    if p2.direction == "up":
        y = p2.ycor()
        p2.sety(y + speed)

    if p2.direction == "down":
        y = p2.ycor()
        p2.sety(y - speed)

    if p2.direction == "left":
        x = p2.xcor()
        p2.setx(x - speed)

    if p2.direction == "right":
        x = p2.xcor()
        p2.setx(x + speed)

def arrow():
    if it == 'red':
        makeredit() 
    if it == 'blue':
        makeblueit()

def contactchecker(it):
    if p1.distance(p2) <= proximity:
        if rounds == True:
            if it == 'red':
                reset()
                p1.direction = "stop"
                p2.direction = "stop"
                return 'blue'
            if it == 'blue':
                p1.direction = "stop"
                p2.direction = "stop"
                reset()
                return 'red'
        
        elif it == 'red':
            p1.goto(601,300)
            p1.direction = "stop"
            return 'blue'
        elif it == 'blue':
            p2.goto(-601,-300)
            p2.direction = "stop"
            return 'red'
    else:
        return it
    
def boundrychecker():
    if p1.ycor() >= yboundry:
        x = p1.xcor()
        y = p1.ycor()
        p1.goto(x,y - yboundry*2  + 21)

    if p1.ycor() <= yboundry*-1:
        x = p1.xcor()
        y = p1.ycor()
        p1.goto(x,y + yboundry*2 - 21)

    if p1.xcor() >= xboundry:
        x = p1.xcor()
        y = p1.ycor()
        p1.goto(x - xboundry*2 + 21,y)

    if p1.xcor() <= xboundry*-1:
        x = p1.xcor()
        y = p1.ycor()
        p1.goto(x+ xboundry*2 ,y)

    if p2.ycor() >= yboundry:
        x = p2.xcor()
        y = p2.ycor()
        p2.goto(x,y - yboundry*2  + 21)

    if p2.ycor() <= yboundry*-1:
        x = p2.xcor()
        y = p2.ycor()
        p2.goto(x,y + yboundry*2 - 21)

    if p2.xcor() >= xboundry:
        x = p2.xcor()
        y = p2.ycor()
        p2.goto(x - xboundry*2 + 21,y)

    if p2.xcor() <= xboundry*-1:
        x = p2.xcor()
        y = p2.ycor()
        p2.goto(x+ xboundry*2 ,y)




game.listen()
game.onkeypress(p1up,"5")
game.onkeypress(p1down,"2")
game.onkeypress(p1left,"1")
game.onkeypress(p1right,"3")
game.onkeypress(p1stop,"0")
game.onkeypress(p2stop,"z")
game.onkeypress(p2up,"w")
game.onkeypress(p2down,"s")
game.onkeypress(p2left,"a")
game.onkeypress(p2right,"d")
game.onkeypress(exit,"q")
game.tracer(1)


if it == 'red':
    makeredit()
elif it == 'blue':
    makeblueit()

while True:
    it = contactchecker(it)
    arrow()
    game.update()
    move() 
    boundrychecker()
    counter2 = timer(counter,counter2)
    counter += 1
    if counter / 50 >= timelimit:
        if it == 'red':
            MB.showinfo("WINNER", "BLUE WINS")
            counter = 0
            counter2 = 0
            reset()
        if it == 'blue':
            MB.showinfo("WINNER", "RED WINS")
            counter = 0
            counter2 = 0
            reset()
