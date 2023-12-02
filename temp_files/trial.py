from tkinter import ttk, Tk

root = Tk()

# Explicitly set the maximum value
progress = ttk.Progressbar(root, length=200, mode="determinate", maximum=100)
progress.pack()

# Set the value to 0
progress["value"] = 30

root.mainloop()
