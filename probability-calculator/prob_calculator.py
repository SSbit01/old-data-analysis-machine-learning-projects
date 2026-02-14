import random


class Hat:
  def __init__(self, **colors):
    self.contents = []
    for i in colors:
      for j in range(colors[i]):
        self.contents.append(i)
    
  def draw(self, num):
    if num >= len(self.contents):
      return self.contents
    
    balls = random.sample(self.contents, k=num)
    for i in balls:
      self.contents.remove(i)
    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  initial_contents = hat.contents.copy()

  hits = 0

  for i in range(num_experiments):
    balls = hat.draw(num_balls_drawn)
    for j in expected_balls:
      if expected_balls[j] > balls.count(j):
        hits += 1
        break
    hat.contents = initial_contents.copy()

  return 1 - hits / num_experiments