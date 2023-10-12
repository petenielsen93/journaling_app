import tkinter as tk
from tkinter import ttk
import ttkbootstrap
import re
import os
from customtkinter import *

root = CTk()
root.geometry("500x400")
root.title('Calendar')

set_appearance_mode("dark")
set_default_color_theme("green")

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
        date_label.configure(text=f"Selected Date: {selected_date}")
        newfile(selected_date)
    else:
        date_label.configure(text="No date entered")

date_label = CTkLabel(master=root, text="Please enter date of journal entry you are trying to access.", text_color="#98FB98")
date_label.place(relx=40, rely=10, anchor="center")
date_label.pack(padx=15, pady=15)


date_entry = CTkEntry(master=root, placeholder_text="Enter date.")
date_entry.place(relx=40, rely=10, anchor="center")
date_entry.pack(padx=15, pady=15)

btn = CTkButton(master=root, text="Open Journal", corner_radius=32, command=open_journal_entry)
btn.place(relx=40, rely=10, anchor="center")
btn.pack(padx=15, pady=15)

root.mainloop()

#add see_date/DateEntry widget, pull date from that to be date for current button?