import turtle 
import math 
screen = turtle.Screen()
screen.bgcolor("black") 
screen.setup(800, 600) 
screen.title("Love Heart") 
screen.tracer(0) 
pen = turtle.Turtle() 
pen.hideturtle() 
pen.speed(0) 
TEXT = "I love you " 
offset = 0 
def heart_points(t, scale=10): 
    x = 16 * math.sin(t) ** 3 
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t) 
    return x * scale, y * scale 
def draw_frame(): 
    global offset 
    pen.clear() 
    t = offset 
    for i in range(250): 
        x, y = heart_points(t) 
        pen.penup() 
        pen.goto(x, y) 
        word = TEXT[i % len(TEXT)].strip() or "love" 
        pen.setheading(math.degrees(math.atan2(-y, x)) + 90) 
        pen.color("white") 
        pen.write(word, align="center", font=("Arial", 13, "bold")) 
        pen.color("#ea80b0") 
        pen.write(word, align="center", font=("Arial", 12, "bold")) 
        t += 0.12 
        offset += 0.03 
        screen.update() 
        screen.ontimer(draw_frame, 16) 
draw_frame() 
screen.mainloop