import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import random

def corrupt_file_random(filename):
    with open(filename, 'wb') as file:
        file_size = os.path.getsize(filename)
        file.seek(0)
        file.write(os.urandom(file_size))
    log_text.insert(tk.END, f"The file '{filename}' has been randomly corrupted.\n")

def corrupt_file_zero(filename):
    with open(filename, 'wb') as file:
        file_size = os.path.getsize(filename)
        file.seek(0)
        file.write(b'\x00' * file_size)
    log_text.insert(tk.END, f"The file '{filename}' has been zero corrupted.\n")

def corrupt_file_truncate(filename):
    with open(filename, 'rb+') as file:
        file_size = os.path.getsize(filename)
        if file_size > 1:
            truncate_size = random.randint(1, file_size)
            file.seek(truncate_size)
            file.truncate()
            log_text.insert(tk.END, f"The file '{filename}' has been truncated and corrupted.\n")
        else:
            log_text.insert(tk.END, f"The file '{filename}' is too small to be truncated and corrupted.\n")

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        corrupt_file_random(file_path)

def select_file_zero_corrupt():
    file_path = filedialog.askopenfilename()
    if file_path:
        corrupt_file_zero(file_path)

def select_file_truncate_corrupt():
    file_path = filedialog.askopenfilename()
    if file_path:
        corrupt_file_truncate(file_path)

def close_window():
    root.destroy()

def show_disclaimer():
    disclaimer_text = """
DISCLAIMER:
This program is for educational purposes only. Use at your own risk.
I'm not responsible for any damages caused by this script.
By using this program, you acknowledge and accept these terms.
    """
    messagebox.showinfo("Disclaimer", disclaimer_text)
    root.deiconify()

root = tk.Tk()
root.withdraw()

show_disclaimer()

root.title("File Corruption Script")

select_button = tk.Button(root, text="Select File to Randomly Corrupt", command=select_file)
select_button.pack(pady=10)

zero_corrupt_button = tk.Button(root, text="Select File to Zero Corrupt", command=select_file_zero_corrupt)
zero_corrupt_button.pack(pady=10)

truncate_corrupt_button = tk.Button(root, text="Select File to Truncate Corrupt", command=select_file_truncate_corrupt)
truncate_corrupt_button.pack(pady=10)

log_text = tk.Text(root, width=50, height=10)
log_text.pack()

line = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
line.pack(fill=tk.X, padx=5, pady=5)

conontron_label = tk.Label(root, text="Made by Conontron")
conontron_label.pack()

root.mainloop()
