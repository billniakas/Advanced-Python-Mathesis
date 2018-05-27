# Animation character 1
# χρησιμοποιεί το φάκελο cartoon


import tkinter as tk
import os

class Animated_character():
    def __init__(self, canvas, dir):
        self.canvas = canvas
        self.canvas_height = int(self.canvas['height'])
        self.canvas_width = int(self.canvas['width'])
        self.images =[]
        try: # φόρτωσε τις εικόνες στη λίστα self.images
            for i in range(len(os.listdir(dir))):
                fname = str(i+1)+'.gif'
                self.images.append(tk.PhotoImage(file=os.path.join(dir,fname)))
        except: return
        self.image_height = self.find_height(self.images)
        self.image_width = self.find_width(self.images)
        self.speed = 400
        self.starting_point = self.canvas_height - margin - self.image_height
        self.current_image = 0
        self.art = self.canvas.create_image(self.canvas_width//2-self.image_width//2,
                            self.starting_point, image=self.images[self.current_image], anchor='nw')
    def next_image(self):
        self.current_image = self.current_image + 1 if self.current_image+1 < len(self.images) else 0
        self.canvas.itemconfig(self.art, image=self.images[self.current_image])
    def move(self):
        if not self.images: return
        self.next_image()  # δείξε την επόμενη εικόνα της σειράς
        self.canvas.after(self.speed, self.move)

    def find_height(self, image_list):
        if image_list: return max([x.height() for x in image_list])
        else: return 0
    def find_width(self, image_list):
        if image_list: return max([x.width() for x in image_list])
        else: return 0

class App():
    def __init__(self, root, **kwargs):
        self.canvas = tk.Canvas(root, width=300, height=300, bg='grey95')
        self.canvas.pack()
        man = Animated_character(self.canvas, 'cartoon' )
        man.move()

margin = 5
root = tk.Tk()
app = App(root)
root.mainloop()
