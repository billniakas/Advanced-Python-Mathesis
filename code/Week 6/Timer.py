# timer

import tkinter as tk
import time

class App():
    def __init__(self, root):
        self.root = root
        self.fnt = ('Arial', 60, 'bold')
        self.f1 = tk.Frame(self.root)
        self.f1.pack(side='top', fill='both', expand=1)
        self.clock = tk.Label(self.f1, font= self.fnt, bg='green', relief='sunken')
        self.clock.pack(fill='both', expand=1)
        self.tick()
    def tick(self):
        s = time.strftime('%H:%M:%S')
        if s != self.clock["text"]:
            self.clock["text"] = s
        self.clock.after(200, self.tick)
root = tk.Tk()
App(root)
root.mainloop()

