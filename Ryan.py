import turtle
t = turtle.Turtle() 
s = turtle.Screen()
t.speed(0)
s.title("3rd Anniversary Of The Friends Popcorn")

turtle.bgcolor("yellow")

# 얼굴
t.begin_fill()
t.color("goldenrod2")
t.circle(200)
t.end_fill()
# 왼쪽 눈썹
t.penup()
t.goto(-145, 250)
t.pendown()
t.width(10)
t.color("black")
t.fd(100)
# 오른쪽 눈썹
t.penup()
t.goto(55, 250)
t.pendown()
t.width(10)
t.color("black")
t.fd(100)
# 왼쪽 눈
t.penup()
t.goto(-80, 185)
t.pendown()
t.begin_fill()
t.circle(18)
t.end_fill()
# 오른쪽 눈
t.penup()
t.goto(85, 185)
t.pendown()
t.begin_fill()
t.circle(18)
t.end_fill()
# 코(1)
t.penup()
t.goto(-20, 100)
for i in range(2):
    t.pendown()
    t.begin_fill()
    t.color("white")
    t.circle(30)
    t.end_fill()
    t.penup()
    t.goto(30, 100)
    t.pendown()
# 코
t.penup()
t.goto(0, 145)
t.pendown()
t.begin_fill()
t.color("black")
t.circle(15)
t.end_fill()
# 귀
t.penup()
t.goto(-155, 310)
t.pendown()
for i in range(2):
    t.begin_fill()
    t.color("goldenrod2")
    t.circle(30)
    t.end_fill()
    t.penup()
    t.goto(155, 310)
    t.pendown()
# 글씨 - H
t.penup()
t.goto(-450, -300)
t.pendown()
t.color("black")
t.setheading(90)
t.fd(150)
t.backward(75)
t.rt(90)
t.fd(50)
t.lt(90)
t.fd(75)
t.backward(150)
# A
t.penup()
t.goto(-350, -300)
t.pendown()
t.rt(15)
t.fd(150)
t.rt(150)
t.fd(150)
t.backward(75)
t.rt(105)
t.fd(38)
# P × 2
t.penup()
t.goto(-220, -300)
t.pendown()
for i in range(2):
    t.setheading(90)
    t.fd(150)
    for j in range(3):
        t.rt(90)
        t.fd(50)
    t.penup()
    t.goto(-120, -300)
    t.pendown()
# Y
t.penup()
t.goto(-5, -300)
t.pendown()
t.setheading(90)
t.fd(95)
t.lt(30)
t.fd(65)
t.backward(65)
t.rt(60)
t.fd(65)
# 3
t.penup()
t.goto(120, -350)
t.pendown()
t.width(50)
t.color("red")
t.setheading(0)
t.fd(150)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(150)
t.backward(150)
t.rt(90)
t.fd(150)
t.lt(90)
t.fd(150)
# rd
t.penup()
t.goto(350, -95)
t.pendown()
t.width(15)
t.setheading(90)
t.fd(50)
t.rt(90)
t.fd(30)
t.penup()
t.goto(430, -95)
t.pendown()
t.setheading(90)
t.fd(50)
t.backward(25)
for i in range(3):
    t.lt(90)
    t.fd(30)
# 하트
t.penup()
t.goto(600, -350)
t.setheading(0)
t.pendown()
t.begin_fill()
t.color("red")
t.lt(45)
t.fd(157)
t.circle(60, 221.37)
t.lt(180)
t.circle(60, 221.37)
t.fd(157)
t.end_fill()
