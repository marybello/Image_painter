from canv import Canvas
from shapes import Square, Rectangle

"""
canvas = Canvas(40, 50, (0,0,0))
r1 = Rectangle(12, 14, 7,9, (100,200,125))
r1.draw(canvas)
s1 = Square(4, 7, 6, (0, 100, 222))
s1.draw(canvas)
"""
print('Welcome to the Math Painting app')
color_of_canvas = input('What background color do you want? black or white?')
if color_of_canvas == 'black':
    color_c = (0, 0, 0)
else:
    color_c = (255, 255, 255)
w_canvas = int(input('What is the width of your image? '))
h_canvas = int(input('What is the height of your image? '))
canvas1 = Canvas(w_canvas, h_canvas, color_c)

while True:

  shape = input('What do you want to draw? enter quit to stop ')
  if shape.lower() == 'square':
      x_square = int(input('Where do you want your square to start from i.e x ? '))
      y_square = int(input('Where do you want your square to start from i.e y ? '))
      l_square = int(input('What is the length of your square? '))
      red = int(input('How much red do you want in your square? '))
      blue = int(input('How much blue do you want in your square? '))
      green = int(input('How much green do you want in your square? '))
      color_s = (red, blue, green)
      square1 = Square(x_square, y_square, l_square, color_s)
      square1.draw(canvas1)
  elif shape.lower() == 'rectangle':
      x_rect = int(input('Where do you want your rectangle to start from i.e x ? '))
      y_rect = int(input('Where do you want your rectangle to start from i.e y ? '))
      w_rect = int(input('What is the width of your rectangle? '))
      h_rect = int(input('What is the height of your rectangle? '))
      red = int(input('How much red do you want in your rectangle? '))
      blue = int(input('How much blue do you want in your rectangle? '))
      green = int(input('How much green do you want in your rectangle? '))
      color_r = (red, blue, green)
      rect1 = Rectangle(x_rect, y_rect, w_rect, h_rect, color_r)
      rect1.draw(canvas1)

  elif shape == 'quit':
      break


canvas1.make('test.png')
