import random
import threading
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

# Run with: python Roulette.py
def show_message():
    while True:
        time.sleep(random.randint(0, 180))
        messagebox.showinfo("Time", "Shot.")

def ask_question():
    while True:
        time.sleep(random.randint(0, 180))
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 100)
        operation = random.choice(['+', '-', '*'])
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2

        user_answer = simpledialog.askinteger("Shot?", f"{num1} {operation} {num2}")
        if user_answer != correct_answer:
            messagebox.showinfo("Wrong Bitch", "Shot.")

threading.Thread(target=show_message, daemon=True).start()
threading.Thread(target=ask_question, daemon=True).start()

while True:
    time.sleep(1)
