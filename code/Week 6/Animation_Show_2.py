# Animation show 2

import tkinter as tk
import random

class App():
    def __init__(self, root):
        self.root = root
        self.width = 400
        self.height = 400
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.balls = [
            Ball(self.canvas, 20, 200, 150, 'red'),
            Ball(self.canvas, 50, 350, 300, 'blue')
        ]
        self.root.after(0, self.animation)
    def animation(self):
        for obj in self.balls:
            obj.move()
        self.root.after(10, self.animation)

class Ball():
    def __init__(self, canvas, r, x=0, y=0, color='white'):
        self.canvas = canvas
        self.id = canvas.create_oval(x-r, y-r, x+r, y+r, fill = color)
        self.vx = random.randint(1,5)
        self.vy = random.randint(1,5)
    def move(self):
        pos = self.canvas.bbox(self.id)
        if pos[0] <= 0 : self.vx = abs(self.vx)
        if pos[1] <= 0 : self.vy = abs(self.vy)
        if pos[2] >= app.width : self.vx = -abs(self.vx)
        if pos[3] >= app.height : self.vy = -abs(self.vy)
        if len(self.canvas.find_overlapping(*pos)) > 1 :
            self.vx = - self.vx
            self.vy = - self.vy
        self.canvas.move(self.id, self.vx, self.vy)

root = tk.Tk()
app = App(root)
root.mainloop()
