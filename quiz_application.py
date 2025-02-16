# create a quiz app in python using GUI

import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.questions = questions
        self.current_question = 0
        self.score = 0
        
        # Configure window
        self.title("Python Quiz")
        self.geometry("500x400")
        
        # Create widgets
        self.question_label = tk.Label(self, wraplength=480)
        self.question_label.pack(pady=10)
        
        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self, 
                variable=self.radio_var,
                value=i
            )
            rb.pack(anchor="w", padx=20)
            self.radio_buttons.append(rb)
        
        self.submit_btn = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_btn.pack(pady=10)
        
        self.score_label = tk.Label(self, text=f"Score: {self.score}/{len(self.questions)}")
        self.score_label.pack()
        
        self.show_question()
    
    def show_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        
        for i, option in enumerate(question_data["options"]):
            self.radio_buttons[i].config(text=option)
        
        self.radio_var.set(-1)  # Deselect all options
    
    def check_answer(self):
        if self.radio_var.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        question_data = self.questions[self.current_question]
        if self.radio_var.get() == question_data["answer"]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}/{len(self.questions)}")
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Completed", 
                              f"Quiz Finished!\nFinal Score: {self.score}/{len(self.questions)}")
            self.destroy()

# Sample questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": 1
    },
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": 0
    },
    {
        "question": "Which planet is known as the Blue Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 0
    }
]

if __name__ == "__main__":
    app = QuizApp(questions)
    app.mainloop()