import tkinter as tk
from customtkinter import CTk, CTkLabel, CTkCanvas

def process_tasks():
    # Simulate processing tasks
    total_tasks = 5
    for task in range(1, total_tasks + 1):
        result_label.configure(text=f"Task {task} Completed")
        update_progress_bar((task / total_tasks) * 100)
        root.update()
        root.after(1000)  # Simulate processing time

def update_progress_bar(value):
    canvas.delete("progress")
    width = 300
    height = 20
    filled_width = (value / 100) * width
    canvas.create_rectangle(0, 0, filled_width, height, fill="#5BC85C", outline="")
    canvas.create_text(width / 2, height / 2, text=f"{int(value)}%", fill="white", font=("Arial", 10), tags="progress")

# Create the main customTkinter window
root = CTk()
root.title("Real-time Results Display")

# Create a label to display real-time results
result_label = CTkLabel(root, text="Results will be displayed here", font=("Arial", 14))
result_label.pack(pady=20)

# Create a custom progress bar using Canvas
canvas = CTkCanvas(root, width=300, height=20, bg="#2B313E")
canvas.pack(pady=10)

# Create a button to start processing tasks
start_button = tk.Button(root, text="Start Processing", command=process_tasks)
start_button.pack()

# Run the customTkinter event loop
root.mainloop()
