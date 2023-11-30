# import customtkinter as ctk
# import tkinter as tk

# root = ctk.CTk()
# root.geometry("1000x550")
# background_image = tk.PhotoImage(file="Assect/back01_big.png")  # Replace with your image file path
# background_label = tk.Label(root, image=background_image)
# background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# time = 0
# Title_Label = ctk.CTkLabel(
#     root, 
#     text="Priority Scheduling(preemptive)",
#     font=("Verdana", 30),
#     corner_radius=20,
#     text_color='#37c9ef',
#     bg_color='#171f28'
# )

# Title_Label.place(x=170,y=10)

# Time_Time = ctk.CTkLabel(
#     root, 
#     text="Time: ",
#     font=("Verdana", 25),
#     corner_radius=20,
#     text_color='#37c9ef',
#     bg_color='#171f28',
# )

# Time_Time.place(x=30,y=100)

# Time_Value = ctk.CTkLabel(
#     root, 
#     text=time,
#     font=("Verdana", 35),
#     corner_radius=20,
#     text_color='#37c9ef',
#     bg_color='#171f28',
# )
# Time_Value.place(x=170,y=95)

# Waiting_Label = ctk.CTkLabel(
#     root, 
#     text="Avg Waiting Time: ",
#     font=("Verdana", 25),
#     corner_radius=20,
#     text_color='#37c9ef',
#     bg_color='#171f28',
# )

# Waiting_Label.place(x=30,y=300)

# TurnAround = ctk.CTkLabel(
#     root, 
#     text="Avg Turn Around Time: ",
#     font=("Verdana", 25),
#     corner_radius=20,
#     text_color='#37c9ef',
#     bg_color='#171f28',
# )

# TurnAround.place(x=30,y=400)


# i = 0
# x = 550
# y = 100

# for k in range(0,3):
#     TurnAround = ctk.CTkLabel(
#         root, 
#         text="T"+str(i),
#         font=("Verdana", 25),
#         corner_radius=20,
#         text_color='#37c9ef',
#         bg_color='#171f28',
#     )
#     TurnAround.place(x=x,y=y)

#     p1 = ctk.CTkProgressBar (
#     root,
#     orientation='horizontal',
#     width=280,
#     height=30,
#     corner_radius=7,
#     progress_color='#2588a2',
#     )   
#     p1.place(x=x+100, y=y)
#     p1.set(0.2)
#     i += 1
#     y += 75


# root.mainloop()


import customtkinter as ctk
import tkinter as tk

class TaskSchedulerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x550")

        # Background Image
        background_image = tk.PhotoImage(file="Assect/back01_big.png")  # Replace with your image file path
        background_label = tk.Label(self, image=background_image)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title Label
        Title_Label = ctk.CTkLabel(
            self, 
            text="Priority Scheduling (preemptive)",
            font=("Verdana", 30),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='#171f28'
        )
        Title_Label.place(x=170, y=10)

        # Time Labels
        Time_Time = ctk.CTkLabel(
            self, 
            text="Time: ",
            font=("Verdana", 25),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='#171f28',
        )
        Time_Time.place(x=30, y=100)

        Time_Value = ctk.CTkLabel(
            self, 
            text=0,
            font=("Verdana", 35),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='#171f28',
        )
        Time_Value.place(x=170, y=95)

        # Other Labels
        Waiting_Label = ctk.CTkLabel(
            self, 
            text="Avg Waiting Time: ",
            font=("Verdana", 25),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='#171f28',
        )
        Waiting_Label.place(x=30, y=300)

        TurnAround = ctk.CTkLabel(
            self, 
            text="Avg Turn Around Time: ",
            font=("Verdana", 25),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='#171f28',
        )
        TurnAround.place(x=30, y=400)

        # Task Labels and Progress Bars
        i = 0
        x = 550
        y = 100

        for k in range(0, 3):
            TurnAround = ctk.CTkLabel(
                self, 
                text="T"+str(i),
                font=("Verdana", 25),
                corner_radius=20,
                text_color='#37c9ef',
                bg_color='#171f28',
            )
            TurnAround.place(x=x, y=y)

            p1 = ctk.CTkProgressBar (
                self,
                orientation='horizontal',
                width=280,
                height=30,
                corner_radius=7,
                progress_color='#2588a2',
            )   
            p1.place(x=x+100, y=y)
            p1.set(0.2)
            i += 1
            y += 75

if __name__ == "__main__":
    app = TaskSchedulerApp()
    app.mainloop()
