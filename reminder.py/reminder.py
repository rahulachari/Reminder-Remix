import tkinter as tk
from tkinter import messagebox
import threading
import time
import datetime
import cv2
import pygame
from PIL import Image, ImageTk

# Play alarm sound
def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")  # Make sure alarm.mp3 is in the same folder
    pygame.mixer.music.play()

# Set the reminder
def set_reminder():
    reminder_text = entry.get()
    reminder_time = time_entry.get()
    try:
        reminder_time = datetime.datetime.strptime(reminder_time, "%H:%M:%S").time()
        current_time = datetime.datetime.now().time()
        delay = (datetime.datetime.combine(datetime.date.today(), reminder_time) - datetime.datetime.combine(datetime.date.today(), current_time)).total_seconds()
        if reminder_text and delay > 0:
            threading.Thread(target=reminder, args=(reminder_text, delay)).start()
        else:
            messagebox.showwarning("Input Error", "Please enter a valid future time.")
    except ValueError:
        messagebox.showwarning("Input Error", "Invalid time format. Use HH:MM:SS")

# Run reminder after delay
def reminder(text, delay):
    time.sleep(delay)
    play_sound()
    messagebox.showinfo("Reminder", text)

# Update video background
def update_background():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (root.winfo_width(), root.winfo_height()))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        bg_label.config(image=img)
        bg_label.image = img
    root.after(33, update_background)  # ~30fps

# Start video capture
cap = cv2.VideoCapture("background.mp4")  # Ensure the video is present

# GUI Window setup
root = tk.Tk()
root.title("Reminder App")
root.geometry("800x600")
root.attributes('-fullscreen', True)
root.attributes("-alpha", 1.0)

# Background video display
bg_label = tk.Label(root)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()
update_background()

# Main reminder input frame
frame = tk.Frame(root, bg="#ffffff", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Labels and Entry fields
tk.Label(frame, text="Reminder Text:", font=("Arial", 14), bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(frame, width=30, font=("Arial", 14), bd=2, relief="solid")
entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Time (HH:MM:SS):", font=("Arial", 14), bg="#ffffff").grid(row=1, column=0, padx=5, pady=5)
time_entry = tk.Entry(frame, width=10, font=("Arial", 14), bd=2, relief="solid")
time_entry.grid(row=1, column=1, padx=5, pady=5)

# Set Reminder button
set_button = tk.Button(
    frame,
    text="Set Reminder",
    command=set_reminder,
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    bd=2,
    relief="raised"
)
set_button.grid(row=2, columnspan=2, pady=10)

# Close app with Esc
root.bind("<Escape>", lambda e: root.destroy())

# Start GUI loop
root.mainloop()

# Release video capture
cap.release()
