# Show image with PhotoImage

import tkinter as tk
class App():
    def __init__(self, root):
        img = tk.PhotoImage(file='python_logo.gif')
        l= tk.Label(root, image = img)
        l.image = img
        l.pack()

root = tk.Tk()
App(root)
root.mainloop()
