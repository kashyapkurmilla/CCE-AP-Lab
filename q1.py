import sys
from tkinter import *

win = Tk()
l1 = Label(text="National Basketball Association", font="times 50")
b1 = Button(win, text="Kobe bryant!", foreground="yellow", background="purple", font="times 25", relief="groove",
            command=sys.exit)

win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=1)
text = Text(win)
text.grid(row=0, column=0, sticky='news')
vert_scroll = Scrollbar(win, orient="vertical")
vert_scroll.grid(row=0, column=1, sticky="ns")
hor_scroll = Scrollbar(win, orient="horizontal")
hor_scroll.grid(row=1, column=0, sticky="ew")
# l1.pack()
# b1.pack()
mainloop()
