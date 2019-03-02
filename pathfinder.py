from PIL import Image
import random

class ElevationsData:
    def __init__(self, width=0, height=0, min=0, max=0, spread=0):
            self.width = width
            self.height = height
            self.min = min
            self.max = max
            self.spread = spread

    def import_elevations_data_me(self, localfile):
        with open(localfile) as file:
                elevations = [line.split() for line in file]
                self.height = len(elevations)
                elevations = [[int(elevation) for elevation in row] for row in elevations]
                self.width = len(elevations)
                return elevations

    def find_min_max_me(self):
        max = self.max
        for a in self:
            for b in a:
                if b > max:
                    max = b
        self.max = max
        min = max
        for c in self:
            for d in c:
                if c < min:
                    min = c
        self.min = min
        self.spread = self.max - self.min

class MapImage:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_canvas_me(dataset):
        self.width = dataset.width
        self.height = dataset.height
        im = Image.new('RGBA', self.width, self.height), 'white')
        return im 

    def paint_canvas_me(canvas, dataset)
        for a in dataset:
            for b in a:
                inputvalue = dataset[a][b]
                outputalpha = (255 * inputvalue)/(dataset.spread)
                r, g, l, q = canvas.getpixel((a,b))
                im.putpixel((a, b), (r, g, l, outputalpha))
    
    def paint_path(canvas, path)
        for a in path:
            for b in a:
                inputvalue = path[a][b]
                im.putpixel((a, b), (path.Rcolor, path.Gcolor, path.Bcolor))



class Path:
    def __init__(self, path, dataset, Rcolor=100, Gcolor=0, Bcolor=0, startx=0, starty=0):
        self.path = path
        self.dataset = datset
        self.Rcolor = Rcolor
        self.Gcolor = Gcolor
        self.Bcolor = Bcolor

    def choose_start_me(self,dataset):
        self.startx = 0
        self.starty = min(dataset[0])
        path = []
        path.append([startx, starty])
        return path
    
    def find_path_me(path):
        while len(path) < dataset.width
        patht.append(FindGreedyNeighbor(path[len(path)-1])
        return path

 

 class Point:
     __init__(self, x, y):
     self.x = x
     self.y = y

    def FindGreedyNeighborFX(x,y):
    choices = [a,c]
    neighbors = []
    neighbors.append(abs(dataset[x+1][y-1]-dataset[x][y]))
    neighbors.append(abs(dataset[x+1][y+0]-dataset[x][y]))
    neighbors.append(abs(dataset[x+1][y+1]-dataset[x][y]))
    a, b, c = neighbors
    minner = min(neighbors)
    if minner == a and minner == c:
        winner = random.choice(choices)
        if winner == a:
            x = x+1
            y = y-1
        else:
            x = x+1
            y = y+1
    elif minner == a:
        x = x+1
        y = y-1
    elif minner == b:
        x = x+1
        y = y+0
    elif minner == c:
        x = x+1
        y = y+1
    return (x,y)


__init__ = "__main__"
elevations = import_elevations_data_me("./elevation_small.txt")
find_min_max_me(elevations)
canvas = create_canvas_me(elevations)
paint_canvas_me(canvas,elevations)
ourpath = choose_start_me(elevations)
foundpath = find_path_me(ourpath)
paint_path(canvas, foundpath)