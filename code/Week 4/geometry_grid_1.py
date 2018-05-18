# grid παράδειγμα 1

import tkinter as tk
class App():
    def __init__(self, root):
        for r in range(4):
            for c in range(4):
                lab = tk.Label(root, width=10, height=5, text='R{}-C{}'.format(r, c),
                            borderwidth=2, relief="raised")
                lab.grid(row=r, column=c)
root = tk.Tk()
App(root)
root.mainloop()
