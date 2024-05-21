import random
import threading
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

def show_message():
    while True:
        time.sleep(random.randint(0, 180))
        messagebox.showinfo("Time", "Shot.")

def ask_question():
    while True:
        time.sleep(random.randint(0, 180))
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*'])
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2

        user_answer = simpledialog.askinteger("Shot?", f"{num1} {operation} {num2}")
        if user_answer != correct_answer:
            messagebox.showinfo("Wrong Bitch", "Drink a Shot.")

threading.Thread(target=show_message, daemon=True).start()
threading.Thread(target=ask_question, daemon=True).start()

while True:
    time.sleep(1)

# To Run: 
# ./run.sh
#  
# To Stop:
# pgrep -f Roulette.py
#
# Copy the ID it gives you and then:
# kill -9 <ID>
