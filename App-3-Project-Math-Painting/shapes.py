class Square:
    """
    this is going to create/draw sqaure objects
    """
    def __init__(self, x, y, l, color):
        self.x = x
        self.y = y
        self.l = l
        self.color = color
    def draw(self, canvas):

        canvas.data[self.x: self.x + self.l, self.y: self.y + self.l] = self.color


class Rectangle:
    """
    this is going to create/draw rectangle objects
    """
    def __init__(self, x,y,w,h,color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self, canvas):

        canvas.data[self.x: self.x + self.w, self.y: self.y + self.y + self.h] = self.color