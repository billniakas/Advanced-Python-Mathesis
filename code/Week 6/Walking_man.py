# walking_man

import tkinter as tk
import os.path

class Animated_character():
    def __init__(self, canvas, dir, size = 0):
        self.canvas = canvas
        self.dir = dir
        self.run = True
        self.canvas_height = int(self.canvas['height'])
        self.canvas_width = int(self.canvas['width'])
        self.images ={'go':[], 'back':[]}
        images = [x for x in os.listdir(self.dir) if x.split('.')[1] == 'gif']
        for _i in range(len(images)):
            file_name = os.path.join(dir, "man"+str(_i+1)+'.gif')
            print(file_name)
            if os.path.isfile(file_name):
                self.images['go'].append(tk.PhotoImage(file=file_name))
            file_name = os.path.join(dir, "man"+str(_i+1)+'rev.gif')
            if os.path.isfile(file_name):
                self.images['back'].append(tk.PhotoImage(file=file_name))
        if size:
            self.zoom(size)
        self.find_max(self.images['go'])  # max height of animated character
        self.direction_x = 50
        self.direction_y = 0
        self.reverse = False
        self.speed = 200
        self.starting_point = self.canvas_height - margin - self.max_height
        self.current_image = 0
        self.art = self.canvas.create_image(0, self.starting_point, image=self.images['go'][self.current_image], anchor='nw')

    def next_image(self):
        self.current_image = self.current_image + 1 if self.current_image+1 < len(self.images['go']) else 0
        img_list = self.images['back'] if self.reverse else self.images['go']
        self.canvas.itemconfig(self.art, image=img_list[self.current_image])

    def find_max(self, image_list):
        self.max_height = max([x.height() for x in image_list])
        print(self.max_height)

    def zoom(self, final):
        # the idea from https://stackoverflow.com/questions/6582387/image-resize-under-photoimage
        self.find_max(self.images['go'])
        initial = self.max_height
        for key in self.images:
            zoomed_images = []
            for im in self.images[key]:
                zoomed_images.append(im.zoom(final//10).subsample(initial//10))
            self.images[key] = zoomed_images

    def move(self):
        self.canvas.move(self.art, self.direction_x , self.direction_y )
        self.next_image()
        coords= self.canvas.bbox(self.art)
        if coords: # έλεγχος για τα όρια του καμβά
            if coords[0] < margin : #αριστερή πλευρά
                self.direction_x = abs(self.direction_x)
            if coords[2] > self.canvas_width-margin: # δεξιά πλευρά
                self.direction_x = -abs(self.direction_x)
            if coords[1] < margin  : # πάνω πλευρά
                self.direction_y = abs(self.direction_y)
            if coords[3] > self.canvas_height-margin: # κάτω πλευρά
                self.direction_y = 0
            if coords[1] < self.starting_point: # if jumped
                self.direction_y = 5
            overlapped_objects = self.canvas.find_overlapping(*coords)
            if len(overlapped_objects)>2: # if more than the obejct itself and the background image
                self.handlecollision(overlapped_objects)
            self.reverse = False if self.direction_x >= 0 else True
            if self.run:
                root.after(self.speed, self.move)
    def handlecollision(self):pass #TODO collision logic
    def start_stop(self, event):
        self.run = False if self.run else True
        self.move()
    def jump(self, event):
        self.direction_y = - 100 # jump up 100 pixels
        print(self.direction_x, self.direction_y)
    def left(self, event):
        self.direction_x = -abs(self.direction_x)
        self.run = True
    def right(self, event):
        self.direction_x = abs(self.direction_x)
        self.run = True


class Scene():
    def __init__(self, root, media, back_image):
        self.back = tk.PhotoImage(file=os.path.join(media, back_image))
        self.width, self.height = self.back.width(), self.back.height()
        self.root = root
        self.root.title('man@Paris')
        self.canvas = tk.Canvas(self.root, width = self.width, heigh = self.height)
        self.canvas.pack()
        self.img = self.canvas.create_image(0,0, image=self.back, anchor='nw')
        self.root.update_idletasks()
        self.root.after(1000, self.create_man)
    def create_man(self):
        self.man = Animated_character(self.canvas, media)
        self.man.move()
        self.root.bind('', self.man.start_stop)
        self.root.bind('', self.man.jump)
        self.root.bind('', self.man.left)
        self.root.bind('', self.man.right)

if __name__ == '__main__' :
    media = 'man'
    root = tk.Tk()
    margin = 50
    scene = Scene(root, media, 'paris.gif')
    root.mainloop()

