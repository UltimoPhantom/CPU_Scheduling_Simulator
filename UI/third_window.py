# import tkinter as tk
# from tkinter import ttk
# import threading
# import time

# class Task:
#     def __init__(self, name, total_steps):
#         self.name = name
#         self.total_steps = total_steps
#         self.current_step = 0

# class TaskStatusUI:
#     def __init__(self, root, tasks):
#         self.root = root
#         self.root.title("Task Status UI")

#         self.tasks = tasks

#         self.task_frames = []
#         for task in self.tasks:
#             frame = ttk.Frame(root, padding="10")
#             frame.pack(pady=5)
            
#             label = ttk.Label(frame, text=f"Task {task.name}")
#             label.grid(row=0, column=0, pady=5)

#             progress_bar = ttk.Progressbar(frame, length=200, mode="determinate", maximum=task.total_steps)
#             progress_bar.grid(row=1, column=0, pady=5)

#             self.task_frames.append((frame, progress_bar))

#         start_button = ttk.Button(root, text="Start Tasks", command=self.start_tasks)
#         start_button.pack(pady=10)

#     def update_task_status(self, task):
#         for frame, progress_bar in self.task_frames:
#             if task.name in frame.winfo_children()[0].cget("text"):
#                 progress_bar["value"] = task.current_step
#                 self.root.update()

#     def start_tasks(self):
#         task_threads = []
#         for task in self.tasks:
#             task_thread = threading.Thread(target=self.run_task, args=(task,))
#             task_thread.start()
#             task_threads.append(task_thread)

#         # Wait for all task threads to finish
#         for task_thread in task_threads:
#             task_thread.join()

#     def run_task(self, task):
#         for _ in range(task.total_steps):
#             time.sleep(1)  # Simulate some work being done
#             task.current_step += 1
#             self.update_task_status(task)

# if __name__ == "__main__":
#     root = tk.Tk()

#     tasks = [Task(name="A", total_steps=10), Task(name="B", total_steps=8), Task(name="C", total_steps=12)]

#     task_status_ui = TaskStatusUI(root, tasks)

#     root.mainloop()
# import tkinter as tk
# from tkinter import ttk
# import threading
# import time

# class Task:
#     def __init__(self, name, total_steps):
#         self.name = name
#         self.total_steps = total_steps
#         self.current_step = 0

# class TaskStatusUI:
#     def __init__(self, root, tasks):
#         self.root = root
#         self.root.title("Task Status UI")

#         self.tasks = tasks

#         self.task_frames = []
#         for task in self.tasks:
#             frame = ttk.Frame(root, padding="10")
#             frame.pack(pady=5)
            
#             label = ttk.Label(frame, text=f"Task {task.name}")
#             label.grid(row=0, column=0, pady=5)

#             progress_bar = ttk.Progressbar(frame, length=200, mode="determinate", maximum=task.total_steps)
#             progress_bar.grid(row=1, column=0, pady=5)

#             self.task_frames.append((frame, progress_bar))

#         start_button = ttk.Button(root, text="Start Tasks", command=self.start_tasks)
#         start_button.pack(pady=10)

#     def update_task_status(self, task):
#         for frame, progress_bar in self.task_frames:
#             if task.name in frame.winfo_children()[0].cget("text"):
#                 progress_bar["value"] = task.current_step
#                 self.root.update()

#     def start_tasks(self):
#         task_threads = []
#         for task in self.tasks:
#             task_thread = threading.Thread(target=self.run_task, args=(task,))
#             task_thread.start()
#             task_threads.append(task_thread)

#         # Wait for all task threads to finish
#         for task_thread in task_threads:
#             task_thread.join()

#     def run_task(self, task):
#         for _ in range(task.total_steps):
#             time.sleep(1)  # Simulate some work being done
#             task.current_step += 1
#             self.update_task_status(task)

# if __name__ == "__main__":
#     root = tk.Tk()

#     tasks = [Task(name="A", total_steps=10), Task(name="B", total_steps=8), Task(name="C", total_steps=12)]

#     task_status_ui = TaskStatusUI(root, tasks)

#     root.mainloop()


import threading
import time
from customtkinter import Tk, Label, Button, Frame, Progressbar

class Task:
    def __init__(self, name, total_steps):
        self.name = name
        self.total_steps = total_steps
        self.current_step = 0

class TaskStatusUI:
    def __init__(self, root, tasks):
        self.root = root
        self.root.title("Task Status UI")

        self.tasks = tasks

        self.task_frames = []
        for task in self.tasks:
            frame = Frame(root, padding="10")
            frame.pack(pady=5)
            
            label = Label(frame, text=f"Task {task.name}")
            label.grid(row=0, column=0, pady=5)

            progress_bar = Progressbar(frame, length=200, mode="determinate", maximum=task.total_steps)
            progress_bar.grid(row=1, column=0, pady=5)

            self.task_frames.append((frame, progress_bar))

        start_button = Button(root, text="Start Tasks", command=self.start_tasks)
        start_button.pack(pady=10)

    def update_task_status(self, task):
        for frame, progress_bar in self.task_frames:
            if task.name in frame.winfo_children()[0].cget("text"):
                progress_bar["value"] = task.current_step
                self.root.update()

    def start_tasks(self):
        task_threads = []
        for task in self.tasks:
            task_thread = threading.Thread(target=self.run_task, args=(task,))
            task_thread.start()
            task_threads.append(task_thread)

        # Wait for all task threads to finish
        for task_thread in task_threads:
            task_thread.join()

    def run_task(self, task):
        for _ in range(task.total_steps):
            time.sleep(1)  # Simulate some work being done
            task.current_step += 1
            self.update_task_status(task)

if __name__ == "__main__":
    root = Tk()

    tasks = [Task(name="A", total_steps=10), Task(name="B", total_steps=8), Task(name="C", total_steps=12)]

    task_status_ui = TaskStatusUI(root, tasks)

    root.mainloop()
