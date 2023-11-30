# import customtkinter as ctk

# class TaskSimulatorApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("Task Simulator")
#         self.geometry("300x200")

#         # Create a progress bar
#         self.progress_bar = ctk.CTkProgressBar(self, mode="determinate")
#         self.progress_bar.set(0)
#         self.progress_bar.pack(pady=10)

#         # Create a button to trigger task processing
#         self.process_button = ctk.CTkButton(self, text="Process Task", command=self.process_task)
#         self.process_button.pack(pady=10)

#     def process_task(self):
#         # Simulate processing a task
#         current_progress = self.progress_bar.get()
#         new_progress = current_progress + 0.1  # Increase progress by 10%

#         # Update the progress bar
#         self.progress_bar.set(new_progress)

#         # Check if all tasks are completed
#         if new_progress == 1.0:
#             self.process_button.configure(state="disabled")
#             self.progress_label.configure(text="All tasks completed!")

#         # Update the progress label
#         self.progress_label.configure(text=f"Progress: {int(new_progress * 100)}%")

# if __name__ == "__main__":
#     app = TaskSimulatorApp()
#     app.mainloop()

import tkinter as tk

class TaskSimulatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Task Simulator")

        # Initialize progress bar variable
        self.progress_value = tk.DoubleVar(value=0.0)

        # Create a progress bar
        self.progress_bar = tk.Progressbar(self, variable=self.progress_value, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack(pady=20)

        # Create a button to simulate processing tasks
        self.process_button = tk.Button(self, text="Process Task", command=self.process_task)
        self.process_button.pack()

    def process_task(self):
        # Increment the progress bar by 10% each time the button is pressed
        current_value = self.progress_value.get()
        new_value = min(current_value + 10, 100)  # Ensure the value doesn't exceed 100%
        self.progress_value.set(new_value)

if __name__ == "__main__":
    app = TaskSimulatorApp()
    app.geometry("300x150")
    app.mainloop()
