# Animation of background

import tkinter as tk

class Background():
    def __init__(self, canvas, *args, **kwargs):
        self.canvas = canvas
        self.back_image = tk.PhotoImage(file= 'skyline.gif')
        self.back_width = self.back_image.width()
        self.back1 = self.canvas.create_image(0,0, image=self.back_image, anchor='nw')
        self.back2 = self.canvas.create_image(self.back_width,0, image=self.back_image, anchor='nw')
        self.canvas_width = int(self.canvas['width'])
        self.canvas_height = int(self.canvas['height'])
        # print(self.canvas_width, self.canvas_height, self.back_width)
        # print('image1', self.canvas.bbox(self.back1))
        # print('image2', self.canvas.bbox(self.back2))
        self.car_image = tk.PhotoImage(file= 'yellow_car.gif')
        self.car = self.canvas.create_image(250,250, image=self.car_image, anchor='nw')
        self.run = 'go'
        self.speed = -5
        self.move_background()

    def move_background(self):
        self.canvas.move(self.back1, self.speed, 0)
        self.canvas.move(self.back2, self.speed, 0)
        coord1 = self.canvas.coords(self.back1)
        coord2 = self.canvas.coords(self.back2)
        if self.run == 'go':
            if max(coord1[0], coord2[0]) <= 0 :
                if coord1[0] < coord2[0]: self.canvas.move(self.back1, self.back_width*2, 0)
                else: self.canvas.move(self.back2, self.back_width*2, 0)
        else:
            if min(coord1[0], coord2[0]) >= 0 :
                if coord1[0] < coord2[0]: self.canvas.move(self.back2, -self.back_width*2, 0)
                else: self.canvas.move(self.back1, -self.back_width*2, 0)
        self.canvas.after(50, self.move_background)
    def toggle(self, e):
        self.run = 'go' if self.run == 'back' else 'back'
        self.speed *= -1

class App():
    def __init__(self, root, **kwargs):
        self.root = root
        self.width=900
        self.height=450
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        b = Background(self.canvas)
        self.canvas.bind('<1>', b.toggle)
root = tk.Tk()
app = App(root)
root.mainloop()
