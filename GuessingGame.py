import tkinter as tk
from tkinter import ttk
import random

class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("300x200")
        
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_instruction = ttk.Label(self, text="Guess a number between 1 and 100:")
        self.label_instruction.grid(column=0, row=0, padx=10, pady=10)
        
        self.guess_input = ttk.Entry(self)
        self.guess_input.grid(column=1, row=0, padx=10, pady=10)
        
        self.guess_button = ttk.Button(self, text="Guess", command=self.check_guess)
        self.guess_button.grid(column=1, row=1, padx=10, pady=10)
        
        self.feedback_label = ttk.Label(self, text="")
        self.feedback_label.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
        
        self.attempts_label = ttk.Label(self, text="Attempts: 0")
        self.attempts_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        
    def check_guess(self):
        try:
            guess = int(self.guess_input.get())
            self.attempts += 1
            
            if guess < self.random_number:
                feedback = "Too low!"
            elif guess > self.random_number:
                feedback = "Too high!"
            else:
                feedback = f"Correct! The number was {self.random_number}."
                feedback += f"\nYou guessed it in {self.attempts} attempts."
                self.guess_button.config(state='disabled')
            
            self.feedback_label.config(text=feedback)
            self.attempts_label.config(text=f"Attempts: {self.attempts}")
        except ValueError:
            self.feedback_label.config(text="Invalid input. Please enter a number.")

if __name__ == "__main__":
    app = GuessingGame()
    app.mainloop()
