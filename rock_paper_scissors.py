import random

while True:

    abbrs = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    combinations = {'r+r': '=', 'r+p': '2', 'r+s': '1',
                    'p+r': '1', 'p+p': '=', 'p+s': '2',
                    's+r': '2', 's+p': '1', 's+s': '=',
                    }

    user = input(f'Enter (r)rock, (p)paper, (s)scissors, or (q)quit: ')
    comp = random.choice(['r', 'p', 's'])

    if user == 'q':
        break

    outcome = combinations[f'{user}+{comp}']

    if outcome == '=':
        print(
            f'You entered {abbrs[user]}, computer entered {abbrs[comp]}. Draw')
    elif outcome == '1':
        print(
            f'You entered {abbrs[user]}, computer entered {abbrs[comp]}. You win')
    elif outcome == '2':
        print(
            f'You entered {abbrs[user]}, computer entered {abbrs[comp]}. Computer win')
