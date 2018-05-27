# Animation character+background

import tkinter as tk
import os
import time
import random

class Animated_character():
    def __init__(self, canvas, dir, size = 0, name =''):
        self.canvas = canvas
        self.name = name
        self.dir = dir
        self.run = True
        self.canvas_height = int(self.canvas['height'])
        self.canvas_width = int(self.canvas['width'])
        self.images ={'go':[], 'back':[]} #go : moving right, back : moving left
        images = [x for x in os.listdir(self.dir) if x.split('.')[1] == 'gif']
        for _i in range(len(images)):
            file_name = os.path.join(dir, self.name+str(_i+1)+'.gif')
            if os.path.isfile(file_name):
                self.images['go'].append(tk.PhotoImage(file=file_name))
            file_name = os.path.join(dir, self.name+str(_i+1)+'rev.gif')
            if os.path.isfile(file_name):
                self.images['back'].append(tk.PhotoImage(file=file_name))
        if size:
            self.zoom(size)
        self.max_height = self.find_max(self.images['go'])  # max height of animated character
        self.reverse = False
        self.speed = 100
        self.starting_point = self.canvas_height - margin - self.max_height
        self.position_x = self.canvas_width//2-self.find_width(self.images['go'])
        self.position_y = self.starting_point
        self.current_image = 0
        self.art = self.canvas.create_image(self.position_x, self.position_y,
                                            image=self.images['go'][self.current_image], anchor='nw')

    def next_image(self):
        self.current_image = self.current_image + 1 if self.current_image+1 < len(self.images['go']) else 0
        img_list = self.images['back'] if self.reverse else self.images['go']
        self.canvas.itemconfig(self.art, image=img_list[self.current_image])

    def find_max(self, image_list):
        return max([x.height() for x in image_list])
    def find_width(self, image_list):
        return max([x.width() for x in image_list])
    def zoom(self, final):
        # the idea from https://stackoverflow.com/questions/6582387/image-resize-under-photoimage
        initial = self.find_max(self.images['go'])
        for key in self.images:
            zoomed_images = []
            for im in self.images[key]:
                zoomed_images.append(im.zoom(final//10).subsample(initial//10))
            self.images[key] = zoomed_images
    def move(self):
        self.next_image()
        if self.position_y < self.starting_point:
            self.position_y +=  10 # gravity
            #self.canvas.coords(self.art, self.position_x, self.position_y)
            self.canvas.move(self.art, 0, 10)
        self.canvas.after(100, self.move)
    def jump(self, event):
        self.position_y -= 60  # πήδημα 60 pixels
        #self.canvas.coords(self.art, self.position_x, self.position_y)
        self.canvas.move(self.art, 0, -60)

class Background():
    def __init__(self, canvas, *args, **kwargs):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.back_image = tk.PhotoImage(file= 'skyline.gif')
        self.back_width = self.back_image.width()
        self.back1 = self.canvas.create_image(0,0, image=self.back_image, anchor='nw')
        self.back2 = self.canvas.create_image(self.back_width,0, image=self.back_image, anchor='nw')
        self.move_background()

    def move_background(self):
        self.canvas.move(self.back1, -5, 0)
        self.canvas.move(self.back2, -5, 0)
        coord1 = self.canvas.coords(self.back1)
        coord2 = self.canvas.coords(self.back2)
        if min(coord1[0], coord2[0]) <= self.canvas_width - self.back_width :
            if coord1[0] < coord2[0]: self.canvas.move(self.back1, self.back_width*2, 0)
            else: self.canvas.move(self.back2, self.back_width*2, 0)
        self.canvas.after(100, self.move_background)

class App():
    def __init__(self, root, **kwargs):
        self.root = root
        self.width=900
        self.height=500
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg='grey70')
        self.canvas.pack()
        b = Background(self.canvas)
        man = Animated_character(self.canvas, 'man', name='man' )
        man.move()
        self.root.bind('', man.jump)

margin = 5
root = tk.Tk()
app = App(root)
root.mainloop()
