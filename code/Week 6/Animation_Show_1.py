# Animation show 1

import tkinter as tk
import time
import random
class ball(object):
    def __init__(self, canvas, *args, **kwargs):
        self.canvas = canvas
        self.id = canvas.create_oval(*args, **kwargs)
        self.vx = random.randint(1,5)
        self.vy = random.randint(1,5)

    def move(self):
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        if x2 > app.width: self.vx = -self.vx
        if y2 > app.height: self.vy = -self.vy
        if x1 < 0: self.vx = -self.vx
        if y1 < 0: self.vy = -self.vy
        self.canvas.move(self.id, self.vx, self.vy)

class App(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self.width = 400
        self.height = 400
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.canvas.pack()
        self.balls = [
            #ball(self.canvas, 20, 260, 120, 360, outline='white', fill='blue'),
            ball(self.canvas, 2, 2, 40, 40, outline='white', fill='red')]
        self.canvas.pack()
        self.master.after(0, self.animation)

    def animation(self):
        for alien in self.balls:
            alien.move()
        self.master.after(12, self.animation)

root = tk.Tk()
app = App(root)
root.mainloop()
