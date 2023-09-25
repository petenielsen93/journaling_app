from datetime import datetime
import os
from tkinter import *
from tkcalendar import *
import re

def sanitize_filename(filename):
    return re.sub(r'[\\/:"*?<>|]+', '', filename)

root=Tk()

def newfile(selected_date):
    #current_date = datetime.now().strftime('%Y-%m-%d')
    sanitized_date = sanitize_filename(selected_date)

    folder_name = "journal_entries"
    file_name = os.path.join(folder_name, f"{sanitized_date}.txt")
    
    # Ensures the folder exists, create it if it doesn't
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    file_exists = os.path.exists(file_name)

    with open(file_name, "a") as file:
        if not file_exists:
            file.write("Journal Entry: " + f"{selected_date}")
        
    os.system(f"notepad {file_name}")

def open_journal_entry():
    selected_date = mycal.get_date()
    #formatted_date = selected_date.strftime('%Y-%m-%d')
    newfile(selected_date)

mycal = Calendar(root, setmode="day")
mycal.pack(padx=15,pady=15)

open_cal=Button(root, text="Open Journal Entry", command=open_journal_entry)
open_cal.pack(padx=15)

root.geometry("300x300")
root.title("Calendar")
root.configure(bg="lightblue")

mainloop()


#Not sure why it is no longer saving each entry into the journal_entries folder, but we have our MVP. Brainstorm on cosmetic and further function changes. 

#if __name__ == "__main__":
    #newfile()  # Call the function to create and save the file in the "journal_entries" folder


