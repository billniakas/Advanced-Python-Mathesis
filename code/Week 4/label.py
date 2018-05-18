#Απλό παράδειγμα με Label

import tkinter as tk
class MyApp():
    def __init__(self, root):
        self.root = root
        self.root.title('Παράδειγα 1b')
        self.widgets()
    def widgets(self):
        self.w = tk.Label(self.root, text=" Καλή σας μέρα!   ", \
                       font = "Arial 36", bg='yellow')
        self.w.pack()

root = tk.Tk() # αρχικό παράθυρο
myapp = MyApp(root)
root.mainloop()
