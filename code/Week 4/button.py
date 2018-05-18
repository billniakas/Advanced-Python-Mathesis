# Button

import tkinter as tk
class MyApp:
    def __init__(self, root):
        self.root = root
        root.title('Παράδειγμα 2')
        self.widgets()
    def widgets(self):
        self.w = tk.Label(self.root, text="  Καλημέρα σας!   ", font = "Arial 30", bg="orange")
        self.w.pack(fill = 'both', expand=1)
        self.b = tk.Button(self.root, text="Exit", font = "Arial 30", command = self.buttonPushed)
        self.b.pack(fill = 'both', expand=1)
    def buttonPushed(self):
        self.root.destroy() # Kill the root window!

root = tk.Tk()
myapp = MyApp(root)
root.mainloop()
