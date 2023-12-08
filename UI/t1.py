import tkinter as tk
import customtkinter as ctk

# Set up the first window
window1 = ctk.CTk()
window1.title("Window 1")
label1 = ctk.CTkLabel(window1, text="This is Window 1")
label1.pack()

# Set size and position for Window 1
window1.geometry("400x200+100+100")  # width x height + x_offset + y_offset

# Set up the second window
window2 = ctk.CTk()
window2.title("Window 2")
label2 = ctk.CTkLabel(window2, text="This is Window 2")
label2.pack()

# Set size and position for Window 2
window2.geometry("400x200+500+100")  # width x height + x_offset + y_offset

# Run the Tkinter event loop
window1.mainloop()
