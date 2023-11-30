import customtkinter as ctk
import time

root = ctk.CTk()
root.geometry("400x300")

p1 = ctk.CTkProgressBar(
    root,
    width=280,
    height=30,
    progress_color='#2588a2',   
)
p1.pack()

# time.sleep(1)

p1.set(.5)

# time.sleep(1)

# p1.step(0.7)

root.mainloop()

time.sleep(1)

p1.set(1)