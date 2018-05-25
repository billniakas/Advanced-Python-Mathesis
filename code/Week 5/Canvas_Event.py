# B1-Motion

import tkinter as tk

class MyApp ():
    def __init__(self, root):
        self.root = root
        root.title("canvas - παράδειγμα B1-Motion")
        root.geometry("800x600+300+300")
        root.resizable(False, False)
        self.create_canvas()

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg='#e0e0ff')
        self.canvas.pack(fill='both', expand=1)
        self.canvas.bind("", self.start_draw)
        self.canvas.bind("", self.draw)

    def start_draw(self, event):
        self.lastx, self.lasty = event.x, event.y

    def draw(self, event):
        self.canvas.create_line(self.lastx, self.lasty, event.x, event.y, width=2)
        self.lastx, self.lasty = event.x, event.y

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == '__main__': main()
