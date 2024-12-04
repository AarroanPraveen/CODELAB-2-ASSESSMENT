from tkinter import *
import random
from tkinter import messagebox


root = Tk()
root.title("Maths Quiz")
root.configure(bg="blue")
root.geometry("500x500")



def generate_mathsproblems(level="Easy"):
    problem_list = []
    for _ in range(10):
        if level == "Easy":
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            operation = random.choice(["+", "-"])
        elif level == "Moderate":
            num1 = random.randint(10, 18)
            num2 = random.randint(10, 18)
            operation = random.choice(["+", "-", "*"])
        elif level == "Advanced":
            num1 = random.randint(1000, 1800)
            num2 = random.randint(1000, 1800)
            operation = random.choice(["+", "-", "*"])

        problem = f"{num1} {operation} {num2}"
        solution = eval(problem)
        problem_list.append((problem, solution))
    return problem_list


def make_questions(question_number=0):
    global question_text, input_field, submit_button, current_index, user_responses

    current_index = question_number
    if question_number < len(problem_set):
        
        for widget in root.winfo_children():
            widget.destroy()

        
        question_text = Label(
            root,
            text=f"Q{question_number + 1}: {problem_set[question_number][0]}",
            font=("Arial", 18),
            bg="black",
            fg="white"
        )
        question_text.pack(pady=10)

        
        input_field = Entry(root, font=("Arial", 14))
        input_field.pack(pady=10)

        
        submit_button = Button(
            root,
            text="SUBMIT ANSWER",
            command=lambda: answer_submission(input_field.get()),
            font=("Arial", 14),
            bg="Black",
            fg="white"
        )
        submit_button.pack(pady=10)
    else:
        calculating_score()


def answer_submission(answer):
    global user_responses, current_index

    if answer.isdigit() or (answer.startswith("-") and answer[1:].isdigit()):
        user_answer = int(answer)
        correct_answer = problem_set[current_index][1]

        if user_answer == correct_answer:
            user_responses.append(user_answer)
        else:
            messagebox.showerror("Incorrect answer Dialougebox", f"INCORRECT ANSWER!!!")

        make_questions(current_index + 1)
    else:
        warning_label = Label(
            root,
            text="Please enter a valid Integer!",
            font=("Arial", 20),
            fg="black",
            bg="orange"
        )
        warning_label.pack(pady=5)

def calculating_score():
    correct_count = sum (1 for i, response in enumerate(user_responses) if response == problem_set[i][1])

  
    for widget in root.winfo_children():
        widget.destroy()

    
    score_display = Label(
        root,
        text=f"You scored: {correct_count} / 10",
        font=("Arial", 18),
        bg="green",
        fg="white"
    )
    score_display.pack(pady=18)

    
    retry_btn = Button(
        root,
        text="Play Again",
        command=display_home_screen,
        font=("Arial", 14),
        bg="green",
        fg="white"
    )
    retry_btn.pack(pady=10)


def start_Easy():
    global problem_set, user_responses
    problem_set = generate_mathsproblems(level="Easy")
    user_responses = []
    make_questions()


def start_Moderate():
    global problem_set, user_responses
    problem_set = generate_mathsproblems(level="Moderate")
    user_responses = []
    make_questions()


def start_Advanced():
    global problem_set, user_responses
    problem_set = generate_mathsproblems(level="Advanced")
    user_responses = []
    make_questions()


def display_home_screen():
    for widget in root.winfo_children():
        widget.destroy()

    
    home_page = Canvas(
        root,
        bg="blue",
        height=300,
        width=290,
        bd=0,
        highlightthickness=0,
        
    )
    home_page.place(x=100, y=0)

    home_page.create_text(
        98.0, 3.0,
        anchor="nw",
        text="Maths Quiz!",
        fill="#FFFFFF",
        font=("Arial", 18 * -1)
    )

    home_page.create_text(
        10.0, 37.0,
        anchor="nw",
        text="Difficulty Level -",
        fill="#FFFFFF",
        font=("Arial", 18)
    )

    
    Button(
        root,
        text="Easy",
        command=start_Easy,
        bg="green",
        fg="white",
        font=("Arial", 18),
        
        
    ).place(x=180, y=69, width=104, height=25)

    Button(
        root,
        text="Moderate",
        command=start_Moderate,
        bg="orange",
        fg="white",
        font=("Arial", 18),
        
        
    ).place(x=180, y=108, width=104, height=25)

    Button(
        root,
        text="Advanced",
        command=start_Advanced,
        bg="red",
        fg="white",
        font=("Arial", 17),
        
       
    ).place(x=180, y=147, width=104, height=25)


display_home_screen()
root.mainloop()
