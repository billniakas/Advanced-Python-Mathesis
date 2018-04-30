class Point():
    ''' ένα σημείο στο καρτεσιανό επίπεδο '''
    the_points = []
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)
        Point.the_points.append(self)

    def distance(self, p):
        return ((self.x - p.x)**2 + (self.y - p.y)**2 )**0.5

# main program
while True:
    coords = input('Συντεταγμένες νέου σημείου (x,y) :')
    if coords =='': break
    if coords.count(',') != 1 : continue
    x,y = coords.split(',')
    if x.isdigit() and y.isdigit():
        new_point = Point(x,y)
        print('Υπάρχουν συνολικά {} σημεία'.format(len(Point.the_points)))
        for p in Point.the_points:
            if p != new_point:
                print('Το σημείο (χ={}, y={}) είναι σε απόσταση {:.2f} από το σημείο'.format(p.x, p.y, p.distance(new_point)))