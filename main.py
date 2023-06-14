import math
from tkinter import *


def percentage_rate(nbr_words):
    """Sets and Calculates percentage rules"""
    best = 80
    percentage = (nbr_words * 100)/best
    return percentage


def result():
    """Checks user performance and provides feedback"""
    global typed_text, n
    # Checking user performance
    typed_text = typing_box.get("1.0", END)
    typed_text = typed_text.split(" ")
    nbr_words = len(typed_text)

    # Providing feedback
    if nbr_words == 1 and typed_text[0] == '\n':
        nbr_words = 0
        canvas.itemconfig(text1, text=f"                        Oops! The time is up!\n\n"
                                      f"                  Your typing speed is: {nbr_words} words/minute\n"
                                      f"                  Your typing quality is on: {percentage_rate(nbr_words)}%",
                          font=("Ariel", 15, "bold"))
        canvas.itemconfig(text2, text=f"You did not type anything, please try again!",
                          font=("Ariel", 15))
    elif nbr_words >= 80:
        canvas.itemconfig(text1, text=f"                        Oops! The time is up!\n\n"
                                      f"                  Your typing speed is: {nbr_words} words/minute\n"
                                      f"                  Your typing quality is on: {percentage_rate(nbr_words)}%",
                          font=("Ariel", 15, "bold"))
        canvas.itemconfig(text2, text=f"Your typing speed is excellent, well done!",
                          font=("Ariel", 15))
    elif 70 <= nbr_words < 80:
        canvas.itemconfig(text1, text=f"                        Oops! The time is up!\n\n"
                                      f"                  Your typing speed is: {nbr_words} words/minute\n"
                                      f"                  Your typing quality is on: {percentage_rate(nbr_words)}%",
                          font=("Ariel", 15, "bold"))
        canvas.itemconfig(text2, text=f"Your typing speed is very good, well done!",
                          font=("Ariel", 15))
    elif 60 <= nbr_words < 70:
        canvas.itemconfig(text1, text=f"                        Oops! The time is up!\n\n"
                                      f"                  Your typing speed is: {nbr_words} words/minute\n"
                                      f"                  Your typing quality is on: {percentage_rate(nbr_words)}%",
                          font=("Ariel", 15, "bold"))
        canvas.itemconfig(text2, text=f"Your typing speed is good, well done!",
                          font=("Ariel", 15))
    elif 50 <= nbr_words < 60:
        canvas.itemconfig(text1, text=f"                        Oops! The time is up!\n\n"
                                      f"                  Your typing speed is: {nbr_words} words/minute\n"
                                      f"                  Your typing quality is on: {percentage_rate(nbr_words)}%",
                          font=("Ariel", 15, "bold"))
        canvas.itemconfig(text2, text=f"Your typing speed is more than an average person",
                          font=("Ariel", 15))
    elif 40 <= nbr_words < 50:
        canvas.itemconfig(text1, text=f"                        Oops! The time is up!\n\n"
                                      f"                  Your typing speed is: {nbr_words} words/minute\n"
                                      f"                  Your typing quality is on: {percentage_rate(nbr_words)}%",
                          font=("Ariel", 15, "bold"))
        canvas.itemconfig(text2, text=f"Your typing speed is average, like the majority of people!",
                          font=("Ariel", 15))
    elif 30 <= nbr_words < 40:
        canvas.itemconfig(text1, text=f"                        Oops! The time is up!\n\n"
                                      f"                  Your typing speed is: {nbr_words} words/minute\n"
                                      f"                  Your typing quality is on: {percentage_rate(nbr_words)}%",
                          font=("Ariel", 15, "bold"))
        canvas.itemconfig(text2, text=f"Your typing speed is bad, you can do better than this!",
                          font=("Ariel", 15))
    elif 20 <= nbr_words < 30:
        canvas.itemconfig(text1, text=f"                        Oops! The time is up!\n\n"
                                      f"                  Your typing speed is: {nbr_words} words/minute\n"
                                      f"                  Your typing quality is on: {percentage_rate(nbr_words)}%",
                          font=("Ariel", 15, "bold"))
        canvas.itemconfig(text2, text=f"Your typing speed is very bad, please work on it!",
                          font=("Ariel", 15))
    else:
        canvas.itemconfig(text1, text=f"                        Oops! The time is up!\n\n"
                                      f"                  Your typing speed is: {nbr_words} words/minute\n"
                                      f"                  Your typing quality is on: {percentage_rate(nbr_words)}%",
                          font=("Ariel", 15, "bold"))
        canvas.itemconfig(text2, text=f"Your typing speed is very poor, You need to work hard on it!",
                          font=("Ariel", 15))


def count_down(count):
    """Calculates and shows timer to the user"""
    global timer, n
    # Creating the timer using math.floor() and Tk.after()
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Placing the timer on the screen
    n += 1
    if n != 1:
        canvas.itemconfig(text1, text=f"                {count_min}:{count_sec}", font=("Ariel", 20, "bold"))
    # Counting down
    if count > 0:
        # Reset the timer
        window.after_cancel(timer)
        # Start the timer
        timer = window.after(1000, count_down, count - 1)

    if count_sec == "00" and n != 1 and count_min == 0:
        canvas.itemconfig(text1, text=f"                Oops! Time is up!", font=("Ariel", 20, "bold"))
        # Checking performance
        result()
        # Remove the MultiText box from the screen
        typing_box.grid_forget()
        # Change button label
        button_label.config(text="Retry")


def typing_started():
    """Takes the user to the typing platform"""
    # Clear the MultiText box
    typing_box.delete('1.0', END)
    # Start timer
    count_down(60)
    # Change the button label
    button_label.config(text="Restart")
    # Remove canvas image
    canvas.itemconfig(canvas_background, image="")
    # Change canvas 2nd text
    canvas.itemconfig(text2,

                      text="You can type the below text or use your own text.\n\n"
                           "Studying is an energy-consuming activity that can make you tired. I have tried out\n"
                           "different methods for energy recovery after studying for hours. Each method has its own\n "
                           "benefits. One of my choices, when I don't have much energy, is eating a light meal in the\n"
                           "evenings. It could be for sure as an energy supply. The other useful method is walking or\n"
                           "jogging in the fresh air. According to my personal experience, this could lead to \n"
                           "recharge my batteries and refresh my mind."
                      )
    # Reset the canvas size
    canvas.config(width=800, height=300)
    # Place the cursor in the MultiText box
    typing_box.focus()
    # place the MultiText box on the screen
    typing_box.grid(row=2, column=0, pady=10)
    # Reset button and button title positions on the screen
    button_label.grid(row=3)
    button.grid(row=4)
    # Change the title
    title_label.config(text="The Typing Speed Test App", font=("Ariel", 20, "bold"))


BG_COLOR = "#B1DDC6"
n = 0
typed_text = ""

# Screen
window = Tk()
window.title("© Cedric Benonga")
window.minsize(width=900, height=450)
window.config(padx=50, pady=10, bg=BG_COLOR)

timer = window.after(0, count_down, 0)

# Canvas
canvas = Canvas(width=800, height=350)
canvas1_nw = PhotoImage(file="images/canvas1_bg.png")
canvas_background = canvas.create_image(400, 175, image=canvas1_nw)
text1 = canvas.create_text(330, 100,
                           text="""
                                For most people, the average number of words per minutes is 40, which the App will 
                                consider as 50% and 80 being 100%. When you're done, the App will tell you the number of 
                                words you are able to type per minute, and what's your percentage based on that.""",
                           font=("Ariel",
                                 12),
                           justify="center")
text2 = canvas.create_text(400, 200,
                           text='When you are ready, please press the "Rabbit" to start.',
                           font=("Ariel", 12),
                           justify="center")
canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0)

# Title label
title_label = Label(text="Welcome to the Typing Speed Test App", font=("Ariel", 20, "bold"))
title_label.grid(row=0, column=0)
title_label.config(bg=BG_COLOR)

# Button label
button_label = Label(text="Start", font=("Ariel", 13, "bold"))
button_label.grid(row=2, column=0)
button_label.config(bg=BG_COLOR)

# Button
start_image = PhotoImage(file="images/start.png")
button = Button(image=start_image, command=typing_started)
button.config(padx=50, pady=4)
button.grid(row=3, column=0, ipadx=5, ipady=5)

# MultiText box
typing_box = Text(height=10, width=50)
typing_box.grid_forget()

window.mainloop()
