# Ζωγραφίζω με splines

DEBUG= False
import tkinter as tk
# a b-spline creator
class App():
    def __init__(self, root):
        self.root = root
        self.root.title('ζωγραφίζω με splines')
        self.points =[]
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg='lightyellow')
        self.canvas.pack()
        self.canvas.bind('<1>', self.add_point)
        self.canvas.bind('', self.create_spline)
    def create_spline(self, e):
        self.canvas.delete('marker')
        self.canvas.delete('poly')
        if DEBUG: print('before', self.points)
        points = list(sum(self.points, ()))
        if DEBUG: print('after', points)
        self.canvas.create_polygon(*points, smooth=1, fill = 'red', tags='spline')
        self.points = []
    def add_point(self, e):
        if self.canvas.find_withtag('spline'):
            self.canvas.delete('spline')
        else:
            self.marker(e)
            self.points.append((e.x,e.y))
            if len(self.points) > 1: self.temp_poly()
    def temp_poly(self):
        points = list(sum(self.points, ()))
        self.canvas.create_line(*points, fill='grey', width=2, tags='poly')

    def marker(self, e):
        self.canvas.create_oval(e.x-5, e.y-5, e.x+5, e.y+5, tags='marker')

root = tk.Tk()
App(root)
root.mainloop()
