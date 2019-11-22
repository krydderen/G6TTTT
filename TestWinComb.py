import numpy as np

# Create a list of all possible win combinations
"""                     1          2          3          4          5          6          7          8  """
win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [6, 3, 0], [7, 4, 1], [8, 5, 2], [6, 4, 2], [8, 4, 0]]


game_state = ["-", "-", "-", "-", "-", "-", "X", "X", "X"]

wincombo = 0

for comb in win_combinations:
    if "-" not in game_state:
        wincombo = 9
    elif game_state[comb[0]] == "X" and game_state[comb[1]] == "X" and game_state[comb[2]] == "X":
        wincombo = (win_combinations.index(comb) + 1)
    elif game_state[comb[0]] == "O" and game_state[comb[1]] == "O" and game_state[comb[2]] == "O":
        wincombo = comb

print(str(wincombo))

print(np.flip(game_state))