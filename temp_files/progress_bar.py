import customtkinter as ctk

root = ctk.CTk()
root.geometry("400x300")

p1 = ctk.CTkProgressBar (
    root,
    orientation='horizontal',
    width=240,
    height=22,
    corner_radius=7,
    progress_color='#2588a2',
)

p1.pack()
p1.set(0)



root.mainloop()
