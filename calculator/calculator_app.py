import tkinter as tk
from tkinter import messagebox

class BasicCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry widget to display the current equation
        self.equation = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.equation, font=('Arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge')
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18), bg='lightblue', command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, char):
        if char == "C":
            self.equation.set("")
        elif char == "=":
            try:
                result = eval(self.equation.get())  # Using eval here for simplicity, but consider a safer alternative.
                self.equation.set(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.equation.set("")
        else:
            current_text = self.equation.get()
            self.equation.set(current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = BasicCalculatorApp(root)

    # Configure grid weights for a 5x4 grid (5 rows, 4 columns)
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()
