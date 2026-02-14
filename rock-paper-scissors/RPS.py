# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    response = {
      "S" : "R",
      "R" : "P",
      "P" : "S"
    }

    guess = "R"

    if prev_play != "": 
      guess = response[prev_play]

    if len(opponent_history) > 4:
      if prev_play == opponent_history[-2] and opponent_history[-3] == opponent_history[-4]:
        guess = prev_play
      
      if len(opponent_history) % 2 == 0 and prev_play == opponent_history[-3]:
        try:
          guess = response[opponent_history[-2]]
        except:
          guess = response[prev_play]

    return guess