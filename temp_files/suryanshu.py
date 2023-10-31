import tkinter as tk
from tkinter import ttk
from tkinter import *

def submit_form():
    num_processes = num_processes_entry.get()
    algorithm = algorithm_var.get()
    source = source_var.get()
    print(num_processes,algorithm,source)

# Create the main window
root = tk.Tk()
root.title("Input Form")

# GUI Measurements
root.geometry("740x493")
root.minsize(740,493)
root.maxsize(740,493)

# GUI Background Image
img_path=PhotoImage(file="bg_img.png")
bg_img=tk.Label(root,image=img_path)
bg_img.place(relheight=1,relwidth=1)

# Headings n all
text_label=tk.Label(root, text='CPU Scheduler',font=('times',24))
text_label.pack()

tk.Label(root, text="", pady=30).pack()

# Number of Processes input
num_processes_label = tk.Label(root, text="Number of Processes:")
num_processes_label.pack()
tk.Label(root, text="", pady=1).pack()
num_processes_entry = tk.Entry(root)
num_processes_entry.pack()
tk.Label(root, text="").pack()

# Scheduling Algorithm input
algorithm_label = tk.Label(root, text="Scheduling Algorithm:")
algorithm_label.pack()
tk.Label(root, text="", pady=1).pack()
algorithm_options = ["FCFS", "Round Robin", "Priority Scheduling"]
algorithm_var = tk.StringVar(root)
algorithm_var.set(algorithm_options[0])
algorithm_dropdown = ttk.Combobox(root, textvariable=algorithm_var, values=algorithm_options)
algorithm_dropdown.pack()
tk.Label(root, text="").pack()

# Data Source input
source_label = tk.Label(root, text="Data Source:")
source_label.pack()
tk.Label(root, text="", pady=1).pack()
source_options = ["Import", "From File", "Random"]
source_var = tk.StringVar(root)
source_var.set(source_options[0])
source_dropdown = ttk.Combobox(root, textvariable=source_var, values=source_options)
source_dropdown.pack()
tk.Label(root, text="").pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()