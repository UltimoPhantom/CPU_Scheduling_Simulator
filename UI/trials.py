import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def draw_gantt_chart():
    root = tk.Tk()
    root.title("Gantt Chart Example")

    fig, ax = plt.subplots()
    tasks = [
        ("Task 1", 10, 30),
        ("Task 2", 50, 20),
        ("Task 3", 100, 40)
    ]
    for i, (label, start, duration) in enumerate(tasks):
        ax.broken_barh([(start, duration)], (10 + 30 * i, 20), facecolors='#4C516D')

    ax.set_xlabel('Time')
    ax.set_yticks([20 + 30 * i for i in range(len(tasks))])
    ax.set_yticklabels([f"Task {i+1}" for i in range(len(tasks))])

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    root.mainloop()

draw_gantt_chart()
