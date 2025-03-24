from turtle import *
import pygame
from time import *
import random
import tkinter as tk
import winsound

try:
    with open("nej_skore.txt", "r", encoding="utf-8") as file:
        content = file.read().strip()
        best_score = int(content) if content else 0
except (FileNotFoundError, ValueError):
    print('\033[91m\n\n[CHYBA]:\n\t Soubor "nej_skore.txt" nebyl nalezen nebo obsahuje neplatná data. \n\t Výchozí hodnota skóre byla nastavena na 0.\n\n\033[0m')
    best_score = 0

try:
    with open("celkovy_cas.txt", "r") as file:
        content = file.read().strip()
        celkovy_cas = float(content) if content else 0
except (FileNotFoundError, ValueError):
    print('\033[91m\n\n[CHYBA]:\n\t Soubor "celkovy_cas.txt" nebyl nalezen nebo obsahuje neplatná data. \n\t Výchozí hodnota času byla nastavena na 0.\n\n\033[0m')
    celkovy_cas = 0
    with open("celkovy_cas.txt", "w") as file:
        file.write("0")
try:
    with open("nej_cas.txt", "r") as file:
        content = file.read().strip()
        best_time = float(content) if content else 0
        best_time = round(best_time, 1)

except (FileNotFoundError, ValueError):
    print('\033[91m\n\n[CHYBA]:\n\t Soubor "nej_cas.txt" nebyl nalezen nebo obsahuje neplatná data. \n\t Výchozí hodnota času byla nastavena na 0.\n\n\033[0m')
    best_time = 0.0
    with open("nej_cas.txt", "w") as file:
        file.write("0")

score = 0

# Add sound file paths
EAT_SOUND = "sounds/eat.wav"
COLLISION_SOUND = "sounds/collision.wav"
WIN_SOUND = "sounds/win.wav"

# Add background music file path
BACKGROUND_MUSIC = "sounds/background.wav"

s = Screen()

canvas = s.getcanvas()
root = canvas.winfo_toplevel()
root.iconbitmap("icons/had.ico")

s.bgcolor("yellow")
s.title(f"Benrod133  |  HÁDEK  |  Skóre: {score}  |  nejlepší skóre = {best_score}")
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

#texty
score_print = Turtle("square")
score_print.color("black")
score_print.penup()
score_print.hideturtle()
score_print.goto(0, 260)
score_print.write(f"Skóre: {score}         nejlepší skóre: {best_score}", align="center", font=("Arial", 18))

nej_cas = Turtle("square")
nej_cas.color("black")
nej_cas.penup()
nej_cas.hideturtle()
nej_cas.goto(0, 200)
nej_cas.write(f"Nejlepší čas: {best_time} s", align="center", font=("Arial", 18))

#čas
actual_time = 0
time_text = Turtle("square")
time_text.color("black")
time_text.penup()
time_text.hideturtle()
time_text.goto(0, 230)
time_text.write(f"Čas: {actual_time} s", align="center", font=("Arial", 18))
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

# Function to play background music
def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load(BACKGROUND_MUSIC)
    pygame.mixer.music.play(-1)

# Function to trigger vibration
def vibrate():
    pass
def force_exit():
    root.destroy()
    exit()
def collided():    
    global continue_game
    global score
    global actual_time
    global head
    global body_parts

    pygame.mixer.music.stop()
    winsound.PlaySound(COLLISION_SOUND, winsound.SND_ASYNC)  # Play collision sound
    sleep(2)
    head.goto(0, 0)
    head.direction = "stop"

    # Skryjeme části těla
    for one_body_part in body_parts:
        one_body_part.goto(1500, 1500)

    # Vyprázdníme list s částmi těla    
    body_parts.clear()
    score = 0
    actual_time = 0  # Reset času

    #nová pozice potravy
    apple_new_pos()

    pygame.mixer.music.play(-1)

def apple_new_pos():
    x = random.randint(-180, 180)
    y = random.randint(-180, 180)
    while (x, y) in [(one_body_part.xcor(), one_body_part.ycor()) for one_body_part in body_parts]:
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
    apple.goto(x, y)
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

# Funkce pro vytvoření joysticku
def create_joystick():
    # Nastavení pozadí obrazovky
    s.bgcolor("gold")
    
    # Vytvoření rámu pro joystick
    joystick_frame = tk.Frame(root, width=600, height=100, bg="lightgray")
    joystick_frame.place(x=0, y=600)  # Joystick bude vždy na pevné pozici ve spodní části okna

    # Vytvoření kruhového joysticku na plátně
    joystick_canvas = tk.Canvas(joystick_frame, width=100, height=100, bg="lightgray", highlightthickness=0)
    joystick_canvas.create_oval(0, 0, 100, 100, fill='gold', outline='yellow', stipple='gray50')
    joystick_canvas.place(x=250, y=0)

    # Tlačítko pro pohyb nahoru
    up_button = tk.Button(joystick_frame, text="↑", command=move_up, bg="gray", activebackground="gray")
    up_button.place(x=285, y=10, width=30, height=30)

    # Tlačítko pro pohyb doleva
    left_button = tk.Button(joystick_frame, text="←", command=move_left, bg="gray", activebackground="gray")
    left_button.place(x=260, y=35, width=30, height=30)

    # Tlačítko pro pohyb dolů
    down_button = tk.Button(joystick_frame, text="↓", command=move_down, bg="gray", activebackground="gray")
    down_button.place(x=285, y=60, width=30, height=30)

    # Tlačítko pro pohyb doprava
    right_button = tk.Button(joystick_frame, text="→", command=move_right, bg="gray", activebackground="gray")
    right_button.place(x=310, y=35, width=30, height=30)

# Vytvoření joysticku
create_joystick()

# bg music spuštění
play_background_music()




fps = 60
#main cyklus
while True:
    try:
        s.update()
        if score > best_score:
            best_score = score
        # kontrola kolize s okrajem okna
        if head.xcor() > 275 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < - 230:
            collided()
        if head.distance(apple) < 20:
            winsound.PlaySound(EAT_SOUND, winsound.SND_ASYNC)  # Play eating sound
            vibrate()
            apple_new_pos()
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
                collided()


        s.title(f"AV®&FatStar a.s.  |  HÁDEK  |  skóre = {score}")
        score_print.clear()
        score_print.write(f"Skóre: {score}         nejlepší skóre: {best_score}", align="center", font=("Arial", 18))
        #zaokrouhlení nej času na 1 desetinné místo
        best_time = round(best_time, 1)
        nej_cas.clear()
        nej_cas.write(f"Nejlepší čas: {best_time} s", align="center", font=("Arial", 18))

        #měření času
        actual_time += 1 / fps  # Přesná akumulace času
        celkovy_cas += 1 / fps  # Přesná akumulace času
        # Zobrazení času zaokrouhleného na 1 desetinné místo
        time_text.clear()
        time_text.write(f"Čas: {round(actual_time, 1)} s", align="center", font=("Arial", 18))

        with open("nej_skore.txt", "w", encoding="utf-8") as file:
            file.write(str(best_score))
        with open("celkovy_cas.txt", "w", encoding="utf-8") as file:
            file.write(str(celkovy_cas))

        if score >= 35:
            continue_game = False
            if actual_time < best_time or best_time == 0.0:
                with open("nej_cas.txt", "w", encoding="utf-8") as file:
                    file.write(str(actual_time))
            pygame.mixer.music.stop()
            s.onkeypress(force_exit, "Escape")
            winsound.PlaySound(WIN_SOUND, winsound.SND_ASYNC)
            def play_again():
                global continue_game
                global best_time
                global score
                global actual_time
                global head
                global body_parts


                win_message.destroy()
                score = 0
                actual_time = 0  # Reset času
                with open("nej_cas.txt", "r", encoding="utf-8") as file:
                    content = file.read().strip()
                    best_time = float(content) if content else 0

                
                head.goto(0, 0)
                head.direction = "stop"
                for one_body_part in body_parts:
                    one_body_part.goto(1500, 1500)
                body_parts.clear()
                apple_new_pos()
                pygame.mixer.music.play(-1)
                continue_game = True

            win_message = tk.Toplevel(root)
            win_message.protocol("WM_DELETE_WINDOW", lambda: None)
            win_message.iconbitmap("icons/win.ico")
            win_message.title("Výhra")
            win_message.geometry("300x150+150+150") 
            tk.Label(win_message, text=f"Vyhrál jsi!\nMaximální dosažitelné skóre: {score}", font=("Arial", 14)).pack(pady=10)
            tk.Button(win_message, text="Hrát znovu", command=play_again).pack(pady=10)
            win_message.transient(root)
            win_message.grab_set()
            root.wait_window(win_message)
        elif score > 34:
            fps = 110               
        elif score > 32:
            fps = 90
        elif score > 30:
            fps = 70
        elif score > 20:
            fps = 50
        elif score > 10:
            fps = 30
        elif score > 5:
            fps = 20
        else:
            fps = 10
        
        pygame.time.Clock().tick(fps)
    except tk.TclError:
        break
def force_exit():
    root.destroy()
    exit()
