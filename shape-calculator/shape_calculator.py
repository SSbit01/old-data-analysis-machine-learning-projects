class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  
  def set_width(self, width):
    self.width = width

  
  def set_height(self, height):
    self.height = height

  
  def get_area(self):
    return self.width * self.height

  
  def get_perimeter(self):
    return 2 * (self.width + self.height)

  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  
  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)

  
  def get_picture(self):
    if any(i > 50 for i in (self.height, self.width)):
      return "Too big for picture."
    
    output = ""
    
    width = ""
    for i in range(self.width):
      width += "*"
    
    for i in range(self.height):
      output += width + "\n"
    
    return output
  
  
  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())



class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  
  def set_side(self, side):
    self.width = side
    self.height = side

  
  def set_width(self, side):
    self.set_side(side)

  
  def set_height(self, side):
    self.set_side(side)

  
  def __str__(self):
    return "Square(side={})".format(self.width)