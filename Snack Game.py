import turtle
import random
import time
delay = 0.1
score=0
high_score = 0
w=turtle.Screen()
w.bgcolor("blue")
w.title("Snake Game")
w.setup(width=600, height=600)
w.tracer(0)
head=turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction="stop"
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0,100)
segments=[]
sc=turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("Score : 0 High Score : 0", align="center",font=("ds-digit", 24, "bold"))
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"
def move():
    if head.direction=="up":
        y=head.ycor()
        y=head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
w.listen()
w.onkeypress(go_up,"w")
w.onkeypress(go_down,"s")
w.onkeypress(go_left,"a")
w.onkeypress(go_right,"d")
while True:
    w.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score =0
        delay=0.1
        sc.clear()
        sc.write("Score : {} High Score : {}".format(score,high_score),align="center",font=("ds-digit", 24, "bold"))
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        delay -=0.001
        score+=10
        if score>high_score:
            high_score=score
        sc.clear()
        sc.write("Score : {} High Score : {}".format(score,high_score),align="center",font=("ds-digit", 24, "bold"))
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            delay= 0.1
            score=0
            sc.clear()
            sc.write("Score : {} High Score : {}".format(score,high_score),align="center",font=("ds-digit", 24, "bold"))
    time.sleep(delay)
w.mainloop()

            
    
    
    
    
        
    
    
            

        
    
