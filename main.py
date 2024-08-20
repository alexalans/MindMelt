import tkinter as tk

class MindMeltApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MindMelt")
        self.root.geometry("500x400")
        self.root.configure(bg="lightblue")

        self.label = tk.Label(root, text="What's on your mind?", font=("Helvetica", 16), bg="lightblue")
        self.label.pack(pady=10)

        self.textbox = tk.Text(root, height=10, width=50, font=("Helvetica", 12), fg="black")
        self.textbox.pack(pady=10)

        self.textbox.bind("<KeyRelease>", self.reset_timer)

        self.color_frame = tk.Frame(root, bg="lightblue")
        self.color_frame.pack(pady=10)

        self.create_color_button("Black", "black")
        self.create_color_button("Red", "red")
        self.create_color_button("Blue", "blue")
        self.create_color_button("Green", "green")
        self.create_color_button("Purple", "purple")

        self.melting_speed = 100  # Speed of text melting in milliseconds
        self.typing_delay = 5000  # Time before text starts disappearing (5 seconds)
        self.timer_id = None

    def create_color_button(self, name, color):
        button = tk.Button(self.color_frame, text=name, bg=color, fg="white", width=8, command=lambda: self.change_text_color(color))
        button.pack(side=tk.LEFT, padx=5)

    def change_text_color(self, color):
        self.textbox.config(fg=color)

    def reset_timer(self, event=None):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.timer_id = self.root.after(self.typing_delay, self.melt_text)

    def melt_text(self):
        current_text = self.textbox.get("1.0", "end-1c")
        if current_text:
            self.melt(current_text, 0)

    def melt(self, text, index):
        if index < len(text):
            self.textbox.delete(f"1.{index}")
            self.root.after(self.melting_speed, self.melt, text, index + 1)
        else:
            self.textbox.delete("1.0", "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = MindMeltApp(root)
    root.mainloop()