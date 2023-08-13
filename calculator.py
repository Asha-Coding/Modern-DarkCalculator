import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font

def calculator():
    def on_button_click(button_value):
        current_text = result_label.cget("text")
        if button_value == "=":
            try:
                result = eval(current_text)
                result_label.config(text=str(result))
            except Exception as e:
                result_label.config(text="Error")
        elif button_value == "C":
            result_label.config(text="")
        else:
            result_label.config(text=current_text + button_value)

    def create_button(frame, button_value, width=1, height=1, font_size=20, bg="#333", fg="#fff"):
        btn_font = font.Font(family="Google Sans", size=font_size)
        return tk.Button(frame, text=button_value, width=width, height=height, font=btn_font, bg=bg, fg=fg,
                        activebackground="#444", activeforeground="#fff",
                        bd=0, highlightthickness=0, relief=tk.RAISED,
                        command=lambda: on_button_click(button_value))

    root = tk.Tk()
    root.title("Modern Calculator")
    root.geometry("300x400")
    root.configure(bg="#444")

    result_label = tk.Label(root, text="", font=("Google Sans", 28), anchor="e", padx=20, pady=10, bg="#222", fg="#fff")
    result_label.pack(fill=tk.X)

    button_frame = tk.Frame(root, bg="#444")
    button_frame.pack(fill=tk.BOTH, expand=True)

    buttons = [
        ("7", 1, 1), ("8", 1, 1), ("9", 1, 1), ("/", 1, 1),
        ("4", 1, 1), ("5", 1, 1), ("6", 1, 1), ("*", 1, 1),
        ("1", 1, 1), ("2", 1, 1), ("3", 1, 1), ("-", 1, 1),
        ("0", 1, 1), (".", 1, 1), ("=", 1, 2), ("+", 1, 1),
        ("C", 1, 1),
    ]

    for i, (button_value, width, height) in enumerate(buttons):
        button = create_button(button_frame, button_value, width, height)
        button.grid(row=i // 4, column=i % 4, sticky="nsew", padx=2, pady=2)
        button_frame.grid_columnconfigure(i % 4, weight=1)
        button_frame.grid_rowconfigure(i // 4, weight=1)

    root.mainloop()

calculator()
