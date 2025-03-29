class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):    
        print(f"({self.x}, {self.y})")
    

point = Point(10, 10)


point.coordinates()