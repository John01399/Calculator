from tkinter import *
from logic import calculate


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg="black")
        self.root.resizable(False, False)

        self.entry = Entry(
            root,
            font=("Helvetica", 32),
            bg="black",
            fg="white",
            bd=0,
            justify="right",
            insertbackground="white"
        )

        self.entry.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="nsew",
            padx=10,
            pady=20
        )

        for i in range(6):
            root.grid_rowconfigure(i, weight=1)

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        self.create_buttons()

        root.bind("<Return>", lambda e: self.equal())
        root.bind("<BackSpace>", lambda e: self.backspace())

    def button_click(self, value):
        self.entry.insert(END, value)

    def clear(self):
        self.entry.delete(0, END)

    def backspace(self):
        current = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, current[:-1])

    def equal(self):
        expression = self.entry.get()
        result = calculate(expression)

        self.entry.delete(0, END)
        self.entry.insert(0, result)

    def create_button(self, text, row, col, bg, command):
        Button(
            self.root,
            text=text,
            font=("Helvetica", 18),
            bg=bg,
            fg="white",
            activebackground=bg,
            activeforeground="white",
            bd=0,
            command=command
        ).grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=3,
            pady=3
        )

    def create_buttons(self):

        number_color = "#333333"
        operator_color = "#FF9F0A"
        special_color = "#A5A5A5"

        buttons = [
            ("C", 1, 0, special_color),
            ("⌫", 1, 1, special_color),
            ("/", 1, 2, operator_color),
            ("*", 1, 3, operator_color),

            ("7", 2, 0, number_color),
            ("8", 2, 1, number_color),
            ("9", 2, 2, number_color),
            ("-", 2, 3, operator_color),

            ("4", 3, 0, number_color),
            ("5", 3, 1, number_color),
            ("6", 3, 2, number_color),
            ("+", 3, 3, operator_color),

            ("1", 4, 0, number_color),
            ("2", 4, 1, number_color),
            ("3", 4, 2, number_color),
            ("=", 4, 3, operator_color),

            ("0", 5, 0, number_color),
            (".", 5, 1, number_color),
        ]

        for text, row, col, color in buttons:

            if text == "C":
                cmd = self.clear

            elif text == "=":
                cmd = self.equal

            elif text == "⌫":
                cmd = self.backspace

            else:
                cmd = lambda t=text: self.button_click(t)

            self.create_button(
                text=text,
                row=row,
                col=col,
                bg=color,
                command=cmd
            )

        # Make 0 button wider
        Button(
            self.root,
            text="0",
            font=("Helvetica", 18),
            bg=number_color,
            fg="white",
            bd=0,
            command=lambda: self.button_click("0")
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=3,
            pady=3
        )