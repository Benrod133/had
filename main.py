from turtle import *
from time import *
import random
import tkinter as tk
import winsound

try:
    with open("nej_skore.txt", "r", encoding="utf-8") as file:
        content = file.read().strip()
        best_score = int(content) if content else 0
except (FileNotFoundError, ValueError):
    best_score = 0
score = 0

# Add sound file paths
EAT_SOUND = "sounds/eat.wav"
COLLISION_SOUND = "sounds/collision.wav"
WIN_SOUND = "sounds/win.wav"

s = Screen()

canvas = s.getcanvas()
root = canvas.winfo_toplevel()
root.iconbitmap("icons/had.ico")

s.bgcolor("yellow")
s.title(f"AV®&FatStar a.s.  |  HÁDEK  |  Skóre: {score}  |  nejlepší skóre = {best_score}")
s.setup(width=600, height=700, startx=(s.window_width() // 2), starty=(s.window_height() // 2 - 400))
s.tracer(False)

s.cv._rootwindow.resizable(False, False)

# Create a top frame for additional information or controls
top_frame = tk.Frame(root, width=600, height=50, bg="lightgray")
top_frame.place(x=0, y=0)

# Adjust the game screen to fit between the top and bottom frames
canvas.place(y=50, width=600, height=600)

#hlava hada

head = Turtle("square")
head.speed(5)
head.color("forest green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#skóre-výpis
score_print = Turtle("square")
score_print.color("black")
score_print.penup()
score_print.hideturtle()
score_print.goto(0, 260)
score_print.write(f"Skóre: {score}         nejlepší skóre: {best_score}", align="center", font=("Arial", 18))

#potrava

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 200)

#tělo
body_parts = []

#funkce
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)

def move_up():
    if head.direction != "down": 
        head.direction = "up"
def move_down():
    if head.direction != "up":  
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":  
        head.direction = "right"

# Function to trigger vibration
def vibrate():
    pass

#eventy
s.listen()
s.onkeypress(move_up, "w")
s.onkeypress(move_down, "s")
s.onkeypress(move_left, "a")
s.onkeypress(move_right, "d")

s.onkeypress(move_up, "Up")
s.onkeypress(move_down, "Down")
s.onkeypress(move_left, "Left")
s.onkeypress(move_right, "Right")

# Create joystick controls for mobile
def create_joystick():
    s.bgcolor("gold")
    joystick_frame = tk.Frame(root, width=600, height=100, bg="lightgray")
    joystick_frame.place(x=0, y=600)  # Adjusted y-coordinate to fit within the window

    # Create a canvas for the round joystick
    joystick_canvas = tk.Canvas(joystick_frame, width=100, height=100, bg="lightgray", highlightthickness=0)
    joystick_canvas.create_oval(0, 0, 100, 100, fill='gold', outline='yellow', stipple='gray50')
    joystick_canvas.place(x=250, y=0)

    up_button = tk.Button(joystick_frame, text="↑", command=move_up, bg="gray", activebackground="gray")
    up_button.place(x=285, y=10, width=30, height=30)

    left_button = tk.Button(joystick_frame, text="←", command=move_left, bg="gray", activebackground="gray")
    left_button.place(x=260, y=35, width=30, height=30)

    down_button = tk.Button(joystick_frame, text="↓", command=move_down, bg="gray", activebackground="gray")
    down_button.place(x=285, y=60, width=30, height=30)

    right_button = tk.Button(joystick_frame, text="→", command=move_right, bg="gray", activebackground="gray")
    right_button.place(x=310, y=35, width=30, height=30)

create_joystick()

#main cyklus
while True:
    try:
        s.update()
        if score > best_score:
            best_score = score
        # kontrola kolize s okrajem okna
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < - 290:
                winsound.PlaySound(COLLISION_SOUND, winsound.SND_ASYNC)  # Play collision sound
                vibrate()
                sleep(2)
                head.goto(0, 0)
                head.direction = "stop"

                # Skryjeme části těla
                for one_body_part in body_parts:
                    one_body_part.goto(1500, 1500)

                # Vyprázdníme list s částmi těla    
                body_parts.clear()
                if score > best_score:
                    best_score = score
                score = 0
        if head.distance(apple) < 20:
            winsound.PlaySound(EAT_SOUND, winsound.SND_ASYNC)  # Play eating sound
            vibrate()
            x = random.randint(-180, 180) 
            y = random.randint(-180, 180) 
            apple.goto(x, y)
            score += 1

            # přidání těla
            new_body_part = Turtle("square")
            new_body_part.color("lime green")
            new_body_part.penup()
            if body_parts:
                # Nastavení pozice za poslední část těla
                last_part = body_parts[-1]
                new_body_part.goto(last_part.xcor(), last_part.ycor())
            else:
                # Pokud tělo neexistuje, nastaví se za hlavu
                new_body_part.goto(head.xcor(), head.ycor())
            body_parts.append(new_body_part)

        if len(body_parts) > 0:
            # Move the last body part to the position of the second-to-last part, and so on
            for index in range(len(body_parts) - 1, 0, -1):
                x = body_parts[index - 1].xcor()
                y = body_parts[index - 1].ycor()
                body_parts[index].goto(x, y)

            # Move the first body part to the head's position
            body_parts[0].goto(head.xcor(), head.ycor())

        move()

        # kolize: hlava -><- tělo
        for one_body_part in body_parts:
            if one_body_part.distance(head) < 5:
                move()
                move()
                sleep(2)
                head.goto(0, 0)
                head.direction = "stop"

                # Skryjeme části těla
                for one_body_part in body_parts:
                    one_body_part.goto(1500, 1500)

                # Vyprázdníme list s částmi těla    
                body_parts.clear()
                score = 0

                #nová pozice potravy
                x = random.randint(-280, 280)
                y = random.randint(-280, 280)
                apple.goto(x, y)

        s.title(f"AV®&FatStar a.s.  |  HÁDEK  |  skóre = {score}")
        score_print.clear()
        score_print.write(f"Skóre: {score}         nejlepší skóre: {best_score}", align="center", font=("Arial", 18))

        with open("nej_skore.txt", "w", encoding="utf-8") as file:
            file.write(str(best_score))

        if score >= 35:
            winsound.PlaySound(WIN_SOUND, winsound.SND_ASYNC)  # Play winning sound
            vibrate()
            win_text = Turtle("square")
            win_text.speed(3)
            win_text.color("black")
            win_text.penup()
            win_text.hideturtle()
            win_text.write("VYHRÁLI JSTE!\nmaximální dosažitelné skóre je: 35 bodů :D", font=("Arial", 20))
            head.direction = "stop"
        elif score > 34:
            sleep(.00005)
        elif score > 32:
            sleep(.0005)
        elif score > 30:
            sleep(.005)
        elif score > 20:
            sleep(.03)
        elif score > 10:
            sleep(.05)
        elif score > 5:
            sleep(.07)
        else:
            sleep(.1)
    except tk.TclError:
        break