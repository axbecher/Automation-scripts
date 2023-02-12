import tkinter as tk
import time
import pyautogui
import os

def start_function():
    root.withdraw()
    delay = float(delay_entry.get())
    time.sleep(delay)
    with open("input.txt", "r") as file:
        text = file.read()
    interval = float(interval_entry.get())
    for char in text:
        pyautogui.press(char)
        time.sleep(interval)
    root.deiconify()
    label.config(text="Terminat!")

def open_file():
    os.startfile("input.txt")

root = tk.Tk()
root.title("Scriere text")
root.geometry("300x500")

label = tk.Label(root, text="", font=("Arial", 24))
label.pack()

start_button = tk.Button(root, text="Start", command=start_function)
start_button.pack()

open_file_button = tk.Button(root, text="Open input.txt", command=open_file)
open_file_button.pack()

interval_label = tk.Label(root, text="Interval (secunde):")
interval_label.pack()

interval_entry = tk.Entry(root)
interval_entry.insert(0, "0.0001")
interval_entry.pack()


delay_label = tk.Label(root, text="Intarziere pana la scriere (secunde):")
delay_label.pack()

delay_entry = tk.Entry(root)
delay_entry.insert(0, "3")
delay_entry.pack()

root.mainloop()