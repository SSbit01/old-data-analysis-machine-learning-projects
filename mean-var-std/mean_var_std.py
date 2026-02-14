import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  calculations = {
    'mean': [],
    'variance': [],
    'standard deviation': [],
    'max': [],
    'min': [],
    'sum': []
  }

  arr = np.array(list).reshape(3, 3)

  for i in (0, 1, None):
    calculations['mean'].append(arr.mean(axis=i).tolist())
    calculations['variance'].append(arr.var(axis=i).tolist())
    calculations['standard deviation'].append(arr.std(axis=i).tolist())
    calculations['max'].append(arr.max(axis=i).tolist())
    calculations['min'].append(arr.min(axis=i).tolist())
    calculations['sum'].append(arr.sum(axis=i).tolist())

  return calculations