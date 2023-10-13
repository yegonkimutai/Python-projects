import random

def roll():
    min = 1
    max = 6
    roll = random.randint(min, max)

    return roll
 
while True:
    players = input('Enter Number of players(1-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print('Must be btwn 1 - 4 players.')
            break
        else:
            print('Invalid choice, try again')
