import turtle

def draw_petal(t, radius, angle):
    """Draws a single petal using two intersecting arcs."""
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

def draw_flower():
    # Setup screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Python Turtle Flower")

    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.hideturtle()

    # --- Draw Stem ---
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.color("green")
    t.pensize(8)
    t.setheading(90)
    t.circle(-150, 40)  # Curved stem

    # --- Draw Outer Petals ---
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pensize(2)

    colors = ["#FF5733", "#FFC300", "#FF1493", "#900C3F", "#DAF7A6", "#C70039"]
    
    petals = 16
    for i in range(petals):
        t.color(colors[i % len(colors)])
        t.begin_fill()
        draw_petal(t, 120, 60)
        t.end_fill()
        t.left(360 / petals)

    # --- Draw Inner Layer ---
    for i in range(petals):
        t.color("gold")
        t.begin_fill()
        draw_petal(t, 60, 60)
        t.end_fill()
        t.left(360 / petals)

    # --- Draw Flower Center ---
    t.penup()
    t.goto(0, 10)
    t.setheading(0)
    t.color("brown", "orange")
    t.pendown()
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    screen.mainloop()

if __name__ == "__main__":
    draw_flower()