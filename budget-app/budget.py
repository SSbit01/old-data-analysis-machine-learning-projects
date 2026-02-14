class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []


  def deposit(self, amount, desc = ""):
    self.ledger.append({"amount": amount, "description": desc})


  def withdraw(self, amount, desc = ""):
    if not self.check_funds(amount):
      return False
    
    self.deposit(-amount, desc)
    
    return True
  
  
  def get_balance(self):
    total = 0
    for i in self.ledger:
      total += i["amount"]
    
    return total
  
  
  def transfer(self, amount, budget):
    if not self.check_funds(amount):
      return False
    
    self.withdraw(amount, "Transfer to " + budget.name)
    budget.withdraw(-amount, "Transfer from " + self.name)
    
    return True
  
  
  def check_funds(self, amount):
    return self.get_balance() >= amount
  
  
  def __str__(self):
    output = ""
    
    stars = ""
    for i in range(round((30 - len(self.name)) / 2)):
      stars += "*"
    output += stars + self.name + stars

    for i in self.ledger:
      desc = i["description"][0:23]
      num = "{:.2f}".format(i["amount"])
      space = ""
      for j in range(30 - len(num) - len(desc)):
        space += " "
      output += "\n" + desc + space + num
    
    output += "\nTotal: " + "{:.2f}".format(self.get_balance())
    
    return output



def create_spend_chart(categories):
  output = "Percentage spent by category"


  total = 0
  category_spending = {}


  for i in categories:
    spending = 0
    
    for j in i.ledger:
      if j["amount"] < 0:
        spending += -j["amount"]
    
    total += spending
    category_spending[i.name] = spending

  
  for i in range(100, -10, -10):
    percen = str(i)
    while len(percen) < 3:
      percen = " " + percen
    output += "\n{}| ".format(percen)

    for j in category_spending:
      if (category_spending[j] / total * 100) >= i:
        output += "o  "
      else:
        output += "   "


  output += "\n    -"
  names = []
  for i in category_spending:
    output += "---"
    while len(i) < len(max(category_spending, key = len)):
      i += " "
    names.append(list(i))
  

  for i in range(len(names[0])):
    output += "\n     "
    for j in names:
      output += j[i] + "  "


  return output