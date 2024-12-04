import tkinter as tk
from tkinter import messagebox, ttk



root = tk.Tk()
root.title("StudentMarks")
root.geometry("800x600")
root.configure(bg="brown")




def File_Entry(file_path="CODE LAB 2 Assignments\Student\studentMarks.txt"):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            student_count = int(lines[0].strip())
            students = []

            for line in lines[1:]:
                parts = line.strip().split(',')
                student_ID = parts[0]
                name = parts[1]
                coursework_marks = list(map(int, parts[2:5]))
                exam_mark = int(parts[5])
                total_coursework = sum(coursework_marks)
                overall_percentage = ((total_coursework + exam_mark) / 160) * 100

                if overall_percentage >= 70:
                    StudentGrade = 'A'
                elif overall_percentage >= 60:
                    StudentGrade = 'B'
                elif overall_percentage >= 50:
                    StudentGrade = 'C'
                elif overall_percentage >= 40:
                    StudentGrade = 'D'
                else:
                    StudentGrade = 'F'

                students.append({
                    "number": student_ID,
                    "name": name,
                    "coursework_total": total_coursework,
                    "exam": exam_mark,
                    "percentage": overall_percentage,
                    "StudentGrade": StudentGrade
                })
            return students, student_count
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {file_path} not found!")
        return [], 0



file_path = "CODE LAB 2 Assignments\Student\studentMarks.txt"
students, student_count = File_Entry(file_path)






def view_all_records():
    Student_records.delete(1.0, tk.END)
    total_percentage = 0

    for student in students:
        Student_records.insert(tk.END, f"Name: {student['name']}\n")
        Student_records.insert(tk.END, f"Number: {student['number']}\n")
        Student_records.insert(tk.END, f"Coursework Total: {student['coursework_total']}\n")
        Student_records.insert(tk.END, f"Exam Mark: {student['exam']}\n")
        Student_records.insert(tk.END, f"Overall Percentage: {student['percentage']:.2f}%\n")
        Student_records.insert(tk.END, f"StudentGrade: {student['StudentGrade']}\n")
        Student_records.insert(tk.END, "-----------------------------------------\n")

        total_percentage += student['percentage']

    average_percentage = total_percentage / student_count
    Student_records.insert(tk.END, f"Total Students: {student_count}\n")
    Student_records.insert(tk.END, f"Average Percentage: {average_percentage:.2f}%\n")


def view_individual_record():
    def display_record():
        name_or_number = entry.get()
        for student in students:
            if name_or_number == student['name'] or name_or_number == student['number']:
                Student_records.delete(1.0, tk.END)
                Student_records.insert(tk.END, f"Name: {student['name']}\n")
                Student_records.insert(tk.END, f"Number: {student['number']}\n")
                Student_records.insert(tk.END, f"Coursework Total: {student['coursework_total']}\n")
                Student_records.insert(tk.END, f"Exam Mark: {student['exam']}\n")
                Student_records.insert(tk.END, f"Overall Percentage: {student['percentage']:.2f}%\n")
                Student_records.insert(tk.END, f"StudentGrade: {student['StudentGrade']}\n")
                return
        messagebox.showinfo("Info", "Student not found!")

    messagebox = tk.Toplevel(root)
    messagebox.title("Show Individual Record")
    tk.Label(messagebox, text="Enter Student Name or Student ID:", bg="purple", fg="white").pack()
    entry = tk.Entry(messagebox)
    entry.pack()
    tk.Button(messagebox, text="Search", command=display_record,bg="Black", fg="yellow", font="arial, 13 bold").pack(pady=5)


def show_highest_score():
    highest = max(students, key=lambda x: x['percentage'])
    Student_records.delete(1.0, tk.END)
    Student_records.insert(tk.END, f"Name: {highest['name']}\n")
    Student_records.insert(tk.END, f"Number: {highest['number']}\n")
    Student_records.insert(tk.END, f"Coursework Total: {highest['coursework_total']}\n")
    Student_records.insert(tk.END, f"Exam Mark: {highest['exam']}\n")
    Student_records.insert(tk.END, f"Overall Percentage: {highest['percentage']:.2f}%\n")
    Student_records.insert(tk.END, f"StudentGrade: {highest['StudentGrade']}\n")


def show_lowest_score():
    lowest = min(students, key=lambda x: x['percentage'])
    Student_records.delete(1.0, tk.END)
    Student_records.insert(tk.END, f"Name: {lowest['name']}\n")
    Student_records.insert(tk.END, f"Number: {lowest['number']}\n")
    Student_records.insert(tk.END, f"Coursework Total: {lowest['coursework_total']}\n")
    Student_records.insert(tk.END, f"Exam Mark: {lowest['exam']}\n")
    Student_records.insert(tk.END, f"Overall Percentage: {lowest['percentage']:.2f}%\n")
    Student_records.insert(tk.END, f"StudentGrade: {lowest['StudentGrade']}\n")



frame = tk.Frame(root)
frame.pack()


buttons = [
    ("View All Records", view_all_records,),
    ("Show Highest Score", show_highest_score),
    ("View Individual Record", view_individual_record),
    ("Show Lowest Score", show_lowest_score)
    
]




for text, command in buttons:
    tk.Button(frame, text=text, command=command, width=20, relief= 'flat', bg="black", fg="white",font="arial, 10 bold", height= 2).pack(side='left')


Student_records = tk.Text(root, width=50, height=16, font=("arial",20))
Student_records.pack(pady=10)


root.mainloop()
