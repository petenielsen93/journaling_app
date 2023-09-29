import tkinter as tk
from tkinter import ttk
import ttkbootstrap
import re
import os

root = ttkbootstrap.Window(themename="cyborg")
root.title('Calendar')

def sanitize_filename(filename):
    return re.sub(r'[\\/:"*?<>|]+', '', filename)

def newfile(selected_date):
    sanitized_date = sanitize_filename(selected_date)
    folder_name = "journal_entries"
    file_name = os.path.join(folder_name, f"{sanitized_date}.txt")

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_exists = os.path.exists(file_name)

    with open(file_name, "a") as file:
        if not file_exists:
            file.write("Journal Entry: " + f"{selected_date}\n")

    os.system(f"notepad {file_name}")

def open_journal_entry():
    selected_date = date_entry.get()
    if selected_date:
        date_label.config(text=f"Selected Date: {selected_date}")
        newfile(selected_date)
    else:
        date_label.config(text="No date entered")

date_label = ttk.Label(root, text="No date entered")
date_label.pack(padx=40, pady=10)

date_entry = ttk.Entry(root)
date_entry.pack(padx=40, pady=10)

btn = ttk.Button(root, text="Open Journal", style="info.TButton", command=open_journal_entry)
btn.pack(padx=40, pady=10)

root.mainloop()

#add see_date/DateEntry widget, pull date from that to be date for current button?