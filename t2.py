import tkinter as tk

root = tk.Tk()
root.title("Calculator")
result_entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), bd=10,
                                     insertwidth=2, width=20, justify="center")
result_entry.grid(row=0, column=0, columnspan=4)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, width=5, height=2)
    button.grid(row=row, column=column, padx=5, pady=5)

root.mainloop()
