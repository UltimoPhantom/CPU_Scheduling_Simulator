import customtkinter as ctk

class TaskSimulatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Task Simulator")
        self.geometry("300x200")

        # Create a progress bar
        self.progress_bar = ctk.CTkProgressBar(self, mode="determinate")
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        # Create a label to display progress status
        self.progress_label = ctk.CTkLabel(self, text="Progress: 0%")
        self.progress_label.pack(pady=10)

        # Initialize a counter for the number of tasks processed
        self.done_counter = 0

        # Start the progress simulation
        self.simulate_progress()

    def simulate_progress(self):
        # Simulate processing tasks
        while self.done_counter < 100:
            # Increase progress by 1%
            self.done_counter += 1
            current_progress = self.progress_bar.get()
            new_progress = current_progress + 0.01

            # Update the progress bar and label
            self.progress_bar.set(new_progress)
            self.progress_label.configure(text=f"Progress: {self.done_counter}%")

            # Wait for a short delay to simulate processing time
            self.after(100, self.simulate_progress)

if __name__ == "__main__":
    app = TaskSimulatorApp()
    app.mainloop()
