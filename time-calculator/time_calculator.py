def add_time(start, duration, weekday = False):
  weekdays = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
  )

  start_splitted = start.split()
  start_num = float(start_splitted[0].replace(":", "."))
  clock = start_splitted[1]
  if clock == "PM":
    start_num += 12

  sum = start_num + float(duration.replace(":", "."))

  if (sum - int(sum)) >= .6:
    sum += .4

  days = 0
  while sum >= 24:
    sum -= 24
    days += 1

  if sum < 12:
    clock = "AM"
    if sum < 1:
      sum += 12
  else:
    clock = "PM"
    if sum >= 13:
      sum -= 12

  sum = round(sum, 2)
  result = "{} {}".format(str(sum).replace(".", ":"), clock)

  if weekday:
    result += ", " + weekdays[(weekdays.index(weekday.lower().capitalize()) + days + 1) % 7 - 1]

  if days == 1:
    result += " (next day)"
  elif days > 1:
    result += " ({} days later)".format(days)

  return result