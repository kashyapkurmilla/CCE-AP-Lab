import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry for displaying the result
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, font=("Arial", 24), bd=10,
                                     insertwidth=2, width=20, justify="center")
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.master, text=text, font=("Arial", 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky="nsew")
            self.master.grid_columnconfigure(column, weight=1)
            self.master.grid_rowconfigure(row, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
