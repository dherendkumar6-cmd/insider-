import time
import turtle

# --- Screen Setup ---
screen = turtle.Screen()
screen.title("Turtle Race Car Animation")
screen.bgcolor("#2e7d32")  # Grass green background
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off auto-updates for smooth frame rendering

# --- Game Variables ---
car_x = 0
car_y = -180
road_stripe_offset = 0
speed = 8

# --- Draw Static Road ---
road_pen = turtle.Turtle()
road_pen.hideturtle()
road_pen.speed(0)

# Main Asphalt Road
road_pen.penup()
road_pen.goto(-200, -300)
road_pen.color("#333333")
road_pen.begin_fill()
for _ in range(2):
    road_pen.forward(400)
    road_pen.left(90)
    road_pen.forward(600)
    road_pen.left(90)
road_pen.end_fill()

# Red/White Side Barriers
for x_pos in [-200, 190]:
    road_pen.penup()
    road_pen.goto(x_pos, -300)
    road_pen.color("#d32f2f")
    road_pen.begin_fill()
    for _ in range(2):
        road_pen.forward(10)
        road_pen.left(90)
        road_pen.forward(600)
        road_pen.left(90)
    road_pen.end_fill()

# --- Dynamic Road Markings Turtle ---
stripe_pen = turtle.Turtle()
stripe_pen.hideturtle()
stripe_pen.speed(0)


def draw_center_stripes(offset):
    stripe_pen.clear()
    stripe_pen.color("#fbc02d")  # Yellow lane markings
    stripe_pen.pensize(6)

    # Draw dashed lines moving downwards based on offset
    for y in range(-300 + int(offset), 320, 60):
        stripe_pen.penup()
        stripe_pen.goto(0, y)
        stripe_pen.pendown()
        stripe_pen.goto(0, y + 30)


# --- Draw Racing Car ---
car_pen = turtle.Turtle()
car_pen.hideturtle()
car_pen.speed(0)


def draw_car(x, y):
    car_pen.clear()

    # Wheels (Black Rectangles)
    car_pen.color("#111111")
    wheel_offsets = [(-32, 25), (22, 25), (-32, -35), (22, -35)]
    for wx, wy in wheel_offsets:
        car_pen.penup()
        car_pen.goto(x + wx, y + wy)
        car_pen.begin_fill()
        for _ in range(2):
            car_pen.forward(10)
            car_pen.left(90)
            car_pen.forward(20)
            car_pen.left(90)
        car_pen.end_fill()

    # Main Body (Red Chassis)
    car_pen.penup()
    car_pen.goto(x - 22, y - 40)
    car_pen.color("#e53935")
    car_pen.begin_fill()
    for _ in range(2):
        car_pen.forward(44)
        car_pen.left(90)
        car_pen.forward(80)
        car_pen.left(90)
    car_pen.end_fill()

    # Front Wing / Nose
    car_pen.penup()
    car_pen.goto(x - 26, y + 35)
    car_pen.color("#b71c1c")
    car_pen.begin_fill()
    for _ in range(2):
        car_pen.forward(52)
        car_pen.left(90)
        car_pen.forward(12)
        car_pen.left(90)
    car_pen.end_fill()

    # Cockpit Windshield (Dark Blue Glass)
    car_pen.penup()
    car_pen.goto(x - 12, y - 10)
    car_pen.color("#0288d1")
    car_pen.begin_fill()
    for _ in range(2):
        car_pen.forward(24)
        car_pen.left(90)
        car_pen.forward(30)
        car_pen.left(90)
    car_pen.end_fill()

    # Racing Stripe
    car_pen.penup()
    car_pen.goto(x - 4, y - 40)
    car_pen.color("#ffffff")
    car_pen.begin_fill()
    for _ in range(2):
        car_pen.forward(8)
        car_pen.left(90)
        car_pen.forward(80)
        car_pen.left(90)
    car_pen.end_fill()


# --- Steering & Control Functions ---
def move_left():
    global car_x
    if car_x > -160:  # Stay inside road boundaries
        car_x -= 20


def move_right():
    global car_x
    if car_x < 160:
        car_x += 20


def speed_up():
    global speed
    if speed < 20:
        speed += 2


def slow_down():
    global speed
    if speed > 2:
        speed -= 2


# --- Keyboard Bindings ---
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(speed_up, "Up")
screen.onkeypress(slow_down, "Down")

# --- Main Animation Loop ---
running = True

while running:
    # Shift road stripes downward to create motion
    road_stripe_offset -= speed
    if road_stripe_offset <= -60:
        road_stripe_offset = 0

    # Redraw frame elements
    draw_center_stripes(road_stripe_offset)
    draw_car(car_x, car_y)

    # Refresh screen display
    screen.update()
    time.sleep(0.02)