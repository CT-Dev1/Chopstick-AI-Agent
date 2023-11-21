'''
Several Required Functions:
1) Generate Move
2) Is Legal

- Take Inspiration from Aggressive Bot

Function 1: Generate Move
- assumes player hands are A and B

'''


def generate_move(state_str):
    state = {'A': int(state_str[1]), 'B': int(state_str[3]), 'C': int(state_str[5]), 'D': int(state_str[7])}
    possible_moves = ['AB', 'AC', 'AD', 'BA', 'BC', 'BD']



