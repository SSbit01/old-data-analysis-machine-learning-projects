def arithmetic_arranger(problems, show_answers = False):
  if (len(problems) > 5):
    return "Error: Too many problems."

  
  line1 = []
  line2 = []
  line3 = []
  line4 = []

  
  for i in problems:
    try:
      result = str(eval(i))
    except:
      return "Error: Numbers must only contain digits."
    
    list = i.split()
    if (list[1] not in {"+", "-"}):
      return "Error: Operator must be '+' or '-'."
    
    max_num = max(list, key=len)
    max_num_length = len(max_num)
    if (max_num_length > 4):
      return "Error: Numbers cannot be more than four digits."
    
    lines = "--"
    for j in range(max_num_length):
      lines += "-"
    lines_length = len(lines)
    
    space1 = ""
    for j in range(lines_length - len(list[0])):
      space1 += " "
    
    space2 = ""
    for j in range(lines_length - len(list[2]) - 1):
      space2 += " "
    
    space4 = ""
    for j in range(lines_length - len(result)):
      space4 += " "
    
    line1.append(space1 + list[0])
    line2.append(list[1] + space2 + list[2])
    line3.append(lines)
    line4.append(space4 + result)


  gap = "    "
  
  output = "{}\n{}\n{}".format(gap.join(line1), gap.join(line2), gap.join(line3))
  
  if show_answers:
    output += "\n" + gap.join(line4)

  
  return output