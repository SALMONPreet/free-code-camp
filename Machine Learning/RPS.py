# This file has the code for the first machine learning problem on freecodecamp executed on gitpod. 
# The name of this file is similar to the one which is to be edited on gitpod.
import random

def player(prev_play, opponent_history=[], transition_table={"": {"R": 0, "P": 0, "S": 0}}):
    
    if prev_play:
        opponent_history.append(prev_play)

    
    last_two = "".join(opponent_history[-2:])

    
    if last_two not in transition_table:
        transition_table[last_two] = {"R": 0, "P": 0, "S": 0}

    
    if len(opponent_history) >= 3:
        prev_seq = "".join(opponent_history[-3:-1])
        if prev_seq not in transition_table:
            transition_table[prev_seq] = {"R": 0, "P": 0, "S": 0}
        transition_table[prev_seq][opponent_history[-1]] += 1

    
    prediction = "R"  # default
    if last_two in transition_table:
        move_probs = transition_table[last_two]
        prediction = max(move_probs, key=move_probs.get)

    
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[prediction]
