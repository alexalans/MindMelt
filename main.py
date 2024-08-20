import tkinter as tk

class MindMeltApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MindMelt")
        self.background = "thistle2"
        self.root.configure(bg=self.background, padx=20, pady=20)

        # Logo

        self.canvas = tk.Canvas()
        self.logo = tk.PhotoImage(file="mindmelt_logo.png")
        self.canvas.config(width=400, height=120, bg=self.background, highlightthickness=0)
        self.canvas.create_image(200, 60, image=self.logo)
        self.canvas.grid(column=1, row=0, columnspan=3, padx=10, pady=10)

        # Textbox
        self.textbox = tk.Text(root, height=15, width=50, font=("Helvetica", 12, "italic"), fg="black", wrap="word", padx=10, pady=10)
        self.textbox.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky="W" + "E" + "N" + "S")
        self.textbox.insert(1.0, "Type your thoughts, worries or secrets here.\n\n"
                                 "Watch them disappear when you stop typing for more than 3 seconds."
                                 "\n\nOr click in the textbox to make your text disappear instantly."
                                 "\n\nClick here to start typing.")
        self.textbox.bind("<KeyRelease>", self.reset_timer)
        self.textbox.bind("<Button-1>", self.clear)

        # Color Buttons
        self.create_color_button("Black", "grey13", 3, 0)
        self.create_color_button("Red", "firebrick3", 3, 1)
        self.create_color_button("Blue", "DodgerBlue2", 3, 2)
        self.create_color_button("Green", "PaleGreen4", 3, 3)
        self.create_color_button("Invisible ink", "white", 3, 4)

        # Configuration
        self.melting_speed = 100  # Speed of text melting in milliseconds
        self.typing_delay = 5000  # Time before text starts disappearing (5 seconds)
        self.timer_id = None

    def create_color_button(self, name, color, row, column):
        if color != "white":
            fg = "white"
        else:
            fg = "black"
        button = tk.Button(self.root, text=name, font=("Helvetica", 11, "bold"), bg=color, fg=fg, width=15, command=lambda: self.change_text_color(color))
        button.grid(row=row, column=column, padx=3, pady=15, sticky="W" + "E" + "N" + "S")

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

    def clear(self, event):
        self.textbox.delete(1.0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = MindMeltApp(root)
    root.mainloop()