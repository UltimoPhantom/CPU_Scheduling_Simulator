# import customtkinter as ctk
# import tkinter as tk
# from PIL import Image, ImageTk
# import time
 
# class Priority_Output(ctk.CTk):
#     def __init__(self,Tasks, Sqe_Result):
#         super().__init__()
#         # print(len(Tasks))
#         self.geometry("1000x550")
#         progress_bar_list = []
#         Tasks = list(Tasks)
#         for i in range(len(Tasks)):
#             Tasks[i][4] = 0  


#         # Main Frame
#         self.main_frame = ctk.CTkFrame(self, width=1000, height=550)
#         self.main_frame.pack_propagate(False)
#         self.main_frame.pack()

#         # Background Image
#         image_path = "Assect/back01_big.png"  # Replace with your image file path
#         img = Image.open(image_path)
#         background_image = ImageTk.PhotoImage(img)
#         background_label = ctk.CTkLabel(self.main_frame, image=background_image, text="")
#         background_label.image = background_image  # To prevent image from being garbage collected
#         background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

#         # Title Label
#         Title_Label = ctk.CTkLabel(
#             self.main_frame, 
#             text="Priority Scheduling (preemptive)",
#             font=("Verdana", 30),
#             corner_radius=20,
#             text_color='#37c9ef',
#             bg_color='#171f28'
#         )
#         Title_Label.place(x=170, y=10)

#         # Time Labels
#         self.time = 0
#         Time_Time = ctk.CTkLabel(
#             self.main_frame, 
#             text="Time: ",
#             font=("Verdana", 25),
#             corner_radius=20,
#             text_color='#37c9ef',
#             bg_color='#171f28',
#         )
#         Time_Time.place(x=30, y=100)

#         self.Time_Value = ctk.CTkLabel(
#             self.main_frame, 
#             text=self.time,
#             font=("Verdana", 35),
#             corner_radius=20,
#             text_color='#37c9ef',
#             bg_color='#171f28',
#         )
#         self.Time_Value.place(x=170, y=95)

#         # Other Labels
#         Waiting_Label = ctk.CTkLabel(
#             self.main_frame, 
#             text="Avg Waiting Time: ",
#             font=("Verdana", 25),
#             corner_radius=20,
#             text_color='#37c9ef',
#             bg_color='#171f28',
#         )
#         Waiting_Label.place(x=30, y=300)

#         TurnAround = ctk.CTkLabel(
#             self.main_frame, 
#             text="Avg Turn Around Time: ",
#             font=("Verdana", 25),
#             corner_radius=20,
#             text_color='#37c9ef',
#             bg_color='#171f28',
#         )
#         TurnAround.place(x=30, y=400)

#         # Task Labels and Progress Bars
#         i = 0
#         x = 550
#         y = 100
        
#         for k in range(len(Tasks)):
#             TurnAround = ctk.CTkLabel(
#                 self.main_frame, 
#                 text=Tasks[k][0],
#                 font=("Verdana", 25),
#                 text_color='#37c9ef',
#                 bg_color='#171f28',
#             )
#             TurnAround.place(x=x, y=y)

#             progress_bar = ctk.CTkProgressBar (
#                 self.main_frame,
#                 orientation='horizontal',
#                 width=280,
#                 height=30,
#                 progress_color='#2588a2',
#             )   
#             progress_bar.place(x=x+100, y=y)
#             progress_bar.set(0.0)
#             progress_bar_list.append(progress_bar)
#             i += 1
#             y += 75
        
                    
#             # for task in Sqe_Result:
#             #     if task != -1:
#             #         for i in range(len(Tasks)):
#             #             if Tasks[i][0] == task:
#             #                 break
#             #         Tasks[i][4] += 1
#             #         progress_bar_list[i].set(Tasks[i][4]%Tasks[i][2])
#             #         time.sleep(1)
#             for i, task in enumerate(Sqe_Result):
#                 if task != -1:
#                     for j in range(len(Tasks)):
#                         if Tasks[j][0] == task:
#                             break
#                     Tasks[j][4] += 1
#                     progress_bar_list[j].set(Tasks[j][4] % Tasks[j][2])
#                     print("**************")
#                     print(Tasks[j][2] % Tasks[j][4])
#                     time.sleep(1)


# # app = Priority_Output()
# # app.mainloop()

import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import time

class Priority_Output(ctk.CTk):
    def __init__(self, Tasks, Sqe_Result):
        super().__init__()
        self.geometry("1000x550")
        self.progress_bar_list = []
        self.Tasks = list(Tasks)
        self.Sqe_Result = Sqe_Result
        for i in range(len(self.Tasks)):
            self.Tasks[i][4] = 0

        # Main Frame
        self.main_frame = ctk.CTkFrame(self, width=1000, height=550)
        self.main_frame.pack_propagate(False)
        self.main_frame.pack()

        # Background Image
        image_path = "Assect/back01_big.png"
        img = Image.open(image_path)
        background_image = ImageTk.PhotoImage(img)
        background_label = ctk.CTkLabel(
            self.main_frame, image=background_image, text=""
        )
        background_label.image = background_image
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title Label
        Title_Label = ctk.CTkLabel(
            self.main_frame, 
            text="Priority Scheduling (preemptive)",
            font=("Verdana", 30),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='#171f28'
        )
        Title_Label.place(x=170, y=10)

        # Time Labels
        self.time = 0
        self.Time_Time = ctk.CTkLabel(
            self.main_frame, 
            text="Time: ",
            font=("Verdana", 25),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='#171f28',
        )
        self.Time_Time.place(x=30, y=100)

        self.Time_Value = ctk.CTkLabel(
            self.main_frame, 
            text=self.time,
            font=("Verdana", 35),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='#171f28',
        )
        self.Time_Value.place(x=170, y=95)

        # Other Labels
        Waiting_Label = ctk.CTkLabel(
            self.main_frame, 
            text="Avg Waiting Time: ",
            font=("Verdana", 25),
            corner_radius=20,
            text_color='#37c9ef',
            bg_color='#171f28',
        )
        Waiting_Label.place(x=30, y=300)

        TurnAround = ctk.CTkLabel(
            self.main_frame, 
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
        
        for k in range(len(Tasks)):
            TurnAround = ctk.CTkLabel(
                self.main_frame, 
                text=Tasks[k][0],
                font=("Verdana", 25),
                text_color='#37c9ef',
                bg_color='#171f28',
            )
            TurnAround.place(x=x, y=y)

            progress_bar = ctk.CTkProgressBar (
                self.main_frame,
                orientation='horizontal',
                width=280,
                height=30,
                progress_color='#2588a2',
            )   
            progress_bar.place(x=x+100, y=y)
            progress_bar.set(0.0)
            self.progress_bar_list.append(progress_bar)
            i += 1
            y += 75
        
    def update_progress_bars(self):
        for i, task in enumerate(self.Sqe_Result):
            if task != -1:
                for j in range(len(self.Tasks)):
                    if self.Tasks[j][0] == task:
                        break
                self.Tasks[j][4] += 1
                self.progress_bar_list[j].set(self.Tasks[j][4] % self.Tasks[j][2])
                print("**************")
                print(self.Tasks[j][2] % self.Tasks[j][4])

        # Check if there are more tasks to update
        if self.Sqe_Result:
            # Schedule the next update after 1000 milliseconds (1 second)
            self.after(1000, self.update_progress_bars)

    def start_updates(self):
        # Start the updates
        self.update_progress_bars()

