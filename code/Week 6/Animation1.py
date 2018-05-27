'''Animation 1: χρήση της after() για κίνηση αντικειμένου στον καμβά'''

import tkinter as tk
DEBUG=False
class App():
    def __init__(self, root):
        self.menu = tk.Frame(root)
        self.menu.pack(side= 'top', fill='both', expand=1)
        self.f = tk.Frame(root)
        self.f.pack(side= 'left', fill='both', expand=1)
        self.width = 600
        self.height = 600
        self.speed = [self.width//100, self.height//100]
        self.display_speed = tk.StringVar()
        self.display_speed.set("{}".format(self.speed[0]))
        self.create_menu()
        self.canvas = tk.Canvas(self.f, width=self.width, height=self.height, bg='lightblue')
        self.canvas.pack(side='left')
        self.r, self.pad = 20, 5
        self.x = self.y = self.r+self.pad
        self.create_ball(self.x,self.y,self.r)
        self.run = False
    def create_menu(self):
        fnt='Arial 30'
        tk.Button(self.menu, text='Go/Stop', font=fnt, command=self.go_stop).pack(side='left', expand=1, fill='both')
        tk.Button(self.menu, text='Reset', font=fnt, command=self.reset).pack(side='left', expand=1, fill='both')
        tk.Button(self.menu, text=' - ', font=fnt, command=self.slower).pack(side='left', expand=1, fill='both')
        tk.Label(self.menu, textvariable=self.display_speed, bg = 'lightyellow',
                width=6, relief='sunken', font = fnt).pack(side='left', fill='both',expand=1, padx=5, pady=5)
        tk.Button(self.menu, text=' + ', bg='yellow', font=fnt ,command=self.speedup).pack(side= 'left', fill='both', expand=1)
    def create_ball(self, x,y,r):
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, tags="thing", fill="red")
    def speedup(self):
        self.speed = [x+1 for x in self.speed]
        self.display_speed.set(str(self.speed[0]))
        if DEBUG: print(self.speed)
    def slower(self):
        print(self.speed)
        self.speed = [x-1 for x in self.speed ]
        self.display_speed.set(str(self.speed[0]))
        if DEBUG: print(self.speed)
    def reset(self):
        self.canvas.delete('thing')
        self.x = self.y = self.r+self.pad
        self.create_ball(self.x, self.y, self.r)
    def go_stop(self):
        self.run = True if not self.run else False
        if DEBUG: print("RUN=", self.run)
        if self.run:  self.move_thing()
    def move_thing(self, *args):
        if self.run:
            if DEBUG: print(*self.speed, self.canvas.bbox("thing"))
            self.canvas.move("thing", *self.speed)
            self.canvas.update_idletasks()
            self.x += self.speed[0] #νέα θέση στον άξονα x
            self.y += self.speed[1] #νέα θέση στον άξονα y
            if self.r+self.pad < self.x < self.width-self.r-self.pad and \
                    self.r+self.pad

