import turtle
import random
import time

delay = 0.1
score=0

#ایجاد صفحه بازی
win = turtle.Screen()
win.title('بازی مار')
win.bgcolor('lightpink')
win.setup(width=600, height=600)
#ترسیم دیوار
wall=turtle.Turtle()
wall.up()
wall.goto(-275,275)
wall.down()
wall.width(3)
for f in range(4):
    wall.fd(550)
    wall.rt(90)
wall.ht()
# ساختن سر مار 
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('darkgreen')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# ساختن غذا برای مار
food = turtle.Turtle()
food.speed(0)
#food.register_shape('imgres_2.gif')
food.shape('circle')
food.color('purple')
food.penup()
food.goto(random.randint(-260,260),random.randint(-260,260))
#امتیاز
wr=turtle.Turtle()
wr.up()
wr.goto(-270,275)
wr.ht()
wr.color('black')
wr.write('امتیاز='+str(score),font=(12))

#ایجاد لیست برای قسمت های بدن
segments = []

# ایجاد تابع برای حرکت مار
def goup():
    head.direction = 'up'

def godown():
    head.direction = 'down'

def goright():
    head.direction = 'right'

def goleft():
    head.direction = 'left'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

# استفاده از کلید کیبرد
win.listen()
win.onkeypress(goup, 'Up')
win.onkeypress(godown, 'Down')
win.onkeypress(goright, 'Right')
win.onkeypress(goleft, 'Left')

while True:
    win.update()

    if head.xcor() > 260 or head.xcor() < -260 or head.ycor() > 260 or head.ycor() < -260:
        time.sleep(1)
        score=score-5
        wr.clear()
        wr.write('امتیاز='+str(score),font=(14))
        head.goto(random.randint(-260,260),random.randint(-260,260))
        head.direction = 'stop'

        # مخفی کردن قسمت های بدن
        for segment in segments:
            segment.goto(1000,1000)

        # پاک کردن قسمت های بدن 
        segments.clear()
        score = 0
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        food.goto(x,y)

    # خوردن غذا و رفتن ان به یک مکان دیگر
    if head.distance(food) < 20:
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        food.goto(x,y)
        

        # اضافه کردن قسمت های بدن 
        newsegment = turtle.Turtle()
        newsegment.speed(0)
        newsegment.shape('circle')
        newsegment.color('green')
        newsegment.penup()
        segments.append(newsegment)
        score = score +10
        wr.clear()
        wr.write('امتیاز='+str(score),font=(14))

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # وصل کردن
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    #برنده شدید
    if score>=50:
        time.sleep(1)
        head.goto(random.randint(-260,260),random.randint(-260,260))
        head.direction = 'stop'
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        food.goto(x,y)
        wr.clear()
        wr.write('شما برنده شدید',font=(14))
              
    move()
    time.sleep(delay)
win.mainloop()