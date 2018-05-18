# grid παράδειγμα 2

import tkinter as tk
class App():
    def __init__(self, root):
        for r in range(4):
            for c in range(4):
                if c == r:
                    lab = tk.Label(root, width=10, height=5, text='R{}-C{}'.format(r, c),
                                borderwidth=5, relief="sunken", bg='yellow')
                    lab.grid(row=r, column=c)
root = tk.Tk()
App(root)
root.mainloop()

