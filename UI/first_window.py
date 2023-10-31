# import customtkinter as ctk
# import tkinter as tk


# def create_first_window():
#     root = ctk.CTk()
#     root.title("CPU Task Scheduler")
#     input_values = {'n': None, 'algo': None}  # Default values


#     main_frame = tk.Frame(root, width=740, height=493)
#     main_frame.pack_propagate(False)
#     main_frame.pack()

#     background_image = tk.PhotoImage(file="Assect/bg_img.png")
#     background_label = tk.Label(main_frame, image=background_image)
#     background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

#     heading_label = ctk.CTkLabel(
#         main_frame,
#         text="CPU Task Scheduler",
#         font=("Courier", 28, 'bold'),
#         bg_color='#343942',
#         text_color='#e9e084',
#         corner_radius=300
#     )
#     heading_label.pack(pady=10)

#     entry1 = ctk.CTkEntry(
#         main_frame, 
#         width=120,
#         height=40, 
#         placeholder_text='Number of tasks',
#         corner_radius=10,
#         bg_color='#1d1c22',
#         placeholder_text_color='#e9e084',
#         font=("Verdana", 12)
#     )
#     entry1.place(x=235, y=90)

    
#     algo_input = ctk.CTkComboBox (
#         main_frame,
#         values= ['Priority', 'Round Robin'],
#         bg_color='#1d1c22',
#         font=("Verdana", 12),
#         dropdown_fg_color= '#1d1c22',
#         dropdown_text_color='#e9e084',
#         text_color='#e9e084',
#         dropdown_hover_color='blue',
#         width=150,
#         height=35
#     )
#     algo_input.place(x=227,y=160)

#     def handleSubmit():
#         n = int(entry1.get())
#         algo = algo_input.get()
#         if (0 <= n <= 10):
#             return (n,algo)
#         else:
#             invalid_label = ctk.CTkLabel(
#                 main_frame,
#                 text='Invalid number of Tasks!!',
#                 text_color='red',
#                 bg_color='#1d1c22'
#             )
#             invalid_label.place(x=220,y=290)
    
#     submitButton = ctk.CTkButton (
#         main_frame,
#         text='Submit',
#         corner_radius=25,
#         fg_color='#e9e084',
#         hover_color='#9c9658',
#         border_color='purple',
#         text_color='black',
#         bg_color='#1d1c22',
#         width=100,
#         height=35,
#         command=handleSubmit
#     )
#     submitButton.place(x=245,y=240)
#     root.mainloop()
#     return 

    

# ans = create_first_window()
# print(ans)

import customtkinter as ctk
import tkinter as tk

class InputWindow:
    def __init__(self):
        self.root = ctk.CTk()
        self.input_values = {'n': None, 'algo': None}
        self.create_first_window()
        
    def handleSubmit(self):
        n = int(self.entry1.get())
        algo = self.algo_input.get()
        if 0 <= n <= 10:
            self.input_values['n'], self.input_values['algo'] = n, algo
            self.root.destroy()
        else:
            invalid_label = ctk.CTkLabel(
                self.main_frame,
                text='Invalid number of Tasks!!',
                text_color='red',
                bg_color='#1d1c22'
            )
            invalid_label.place(x=220, y=290)
    
    def create_first_window(self):
        self.root.title("CPU Task Scheduler")

        self.main_frame = tk.Frame(self.root, width=740, height=493)
        self.main_frame.pack_propagate(False)
        self.main_frame.pack()

        background_image = tk.PhotoImage(file="Assect/bg_img.png")  # Replace with your image file path
        background_label = tk.Label(self.main_frame, image=background_image)
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.entry1 = ctk.CTkEntry(
            self.main_frame,
            width=120,
            height=40,
            placeholder_text='Number of tasks',
            corner_radius=10,
            bg_color='#1d1c22',
            placeholder_text_color='#e9e084',
            font=("Verdana", 12)
        )
        self.entry1.place(x=235, y=90)

        self.algo_input = ctk.CTkComboBox(
            self.main_frame,
            values=['Priority', 'Round Robin'],
            bg_color='#1d1c22',
            font=("Verdana", 12),
            dropdown_fg_color='#1d1c22',
            dropdown_text_color='#e9e084',
            text_color='#e9e084',
            dropdown_hover_color='blue',
            width=150,
            height=35
        )
        self.algo_input.place(x=227, y=160)

        submitButton = ctk.CTkButton(
            self.main_frame,
            text='Submit',
            corner_radius=25,
            fg_color='#e9e084',
            hover_color='#9c9658',
            border_color='purple',
            text_color='black',
            bg_color='#1d1c22',
            width=100,
            height=35,
            command=self.handleSubmit
        )
        submitButton.place(x=245, y=240)
        
        self.root.mainloop()

    def get_input_values(self):
        return self.input_values

# Create the window and get the values
# input_window = InputWindow()
# values = input_window.get_input_values()
# print(values)


