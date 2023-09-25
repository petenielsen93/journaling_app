from datetime import datetime
import os

def newfile():
    current_date = datetime.now().strftime('%Y-%m-%d')
    folder_name = "journal_entries"
    file_name = os.path.join(folder_name, f"{current_date}.txt")
    
    # Ensure the folder exists, create it if it doesn't
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    file_exists = os.path.exists(file_name)

    with open(file_name, "a") as file:
        if not file_exists:
            file.write("Journal Entry: " + f"{current_date}")
        
    os.system(f"notepad {file_name}")

if __name__ == "__main__":
    newfile()  # Call the function to create and save the file in the "journal_entries" folder


#with this, I create a text file and save it in the root folder. Next I want to save it in a specific folder as a text file. 
#after that, I want to add this to the tkinter calendar, get and assign each day to a file, create a button that allows you to
#open a file for that date/save it/reopen