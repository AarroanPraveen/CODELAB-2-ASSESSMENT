from tkinter import *
import random


root = Tk()
root.geometry("450x450")
root.title("Alexa joke")
root.configure(bg="cyan")


def make_jokes(file_path="CODE LAB 2 Assignments\Alexa/randomjoke.txt"):
    try:
        with open(file_path, "r") as random_joke_file:
            random_joke_list = [line.strip().split("-") for line in random_joke_file.readlines() if "?" in line]
        return random_joke_list
    except FileNotFoundError:
        return []


def navigate_to_joke_page():
    random_joke_label.config(text="Press The Button to Hear a Joke!")
    random_joke_label.place(relx=0.5, rely=0.70, anchor=CENTER)

    random_joke_button.config(text="Alexa tell me a joke", command=show_random_joke)
    random_joke_button.place(relx=0.5, rely=0.88, anchor=CENTER)

    Showrandom_joke_button.place(relx=0.87, rely=0.88, anchor=CENTER)
    exit_button.place(relx=0.1, rely=0.88, anchor=CENTER)


def show_random_joke():
    global active_random_joke
    if random_jokess:
        active_random_joke = random.choice(random_jokess)
        random_joke_label.config(text=active_random_joke[0])
    else:
        random_joke_label.config(text="No jokes available.")
        active_random_joke = None


def show_ShowJoke():
    if active_random_joke:
        random_joke_label.config(text=active_random_joke[1])
    else:
        random_joke_label.config(text="No ShowJoke to display.")



random_jokess = make_jokes()
active_random_joke = None


background_thing = Canvas(
    root,
    bg="cyan",
    height=278,
    width=400,
    highlightthickness=0,
    
)
background_thing.place(x=0, y=0)

random_joke_button = Button(
    root,
    text="Alexa tell me a joke",
    font=("Arial 15 bold"),
    fg="white",
    bg="magenta",
    command=navigate_to_joke_page
)
random_joke_button.place(relx=0.5, rely=0.88, anchor=CENTER, y=-150,)

Showrandom_joke_button = Button(
    root,
    text="Show Joke",
    fg="white",
    bg="#30ABCA",
    font=("Arial 15 bold"),
    command=show_ShowJoke
)
Showrandom_joke_button.place_forget()

exit_button = Button(
    root,
    text="Quit Joke",
    fg="white",
    bg="Gold",
    font=("Arial 15 bold"),
    command=root.quit
)
exit_button.place_forget()

random_joke_label = Label(
    root,
    text="Press the below button to Hear the Jokes",
    font=("Arial 15 bold"),
    fg="white",
    bg="hotpink",
    wraplength=350,
    justify="center"
)
random_joke_label.place(relx=0.5, rely=0.69, anchor=CENTER, y=-199,)


root.mainloop()
