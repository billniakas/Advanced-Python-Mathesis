# Πειραματισμός με την
# Φαινόμενο ελαστικού ορθογωνίου

import tkinter as tk

class MyApp():
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        self.rubberbandBox = None
        self.canvas.bind("", self.mouse_down)
        self.canvas.bind( "", self.mouse_motion)
        self.canvas.bind( "", self.mouse_up)
    def mouse_down(self, event):
        self.startx = event.x
        self.starty = event.y
        self.rubberbandBox = self.canvas.create_rectangle(self.startx, self.starty, event.x, event.y)
    def mouse_motion(self, event):
        self.canvas.coords(self.rubberbandBox, self.startx, self.starty, event.x, event.y)
    def mouse_up(self, event):
        self.canvas.create_rectangle(*self.canvas.coords(self.rubberbandBox), width=2, fill='blue')
        self.canvas.delete(self.rubberbandBox)
def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == '__main__': main()
