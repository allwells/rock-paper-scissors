# # # # # # # # # # # # # # # # # # # # # # # #
#                                             #
#   Rock Paper Scissors Game - Zuri Training  #
#                                             #
#   @author Allwell Onen                      #
#   Wednesday, 1st June 2022                  #
#                                             #
# # # # # # # # # # # # # # # # # # # # # # # #

from time import sleep
import random


rock = """
    _____
___/  ___)
     (____)
     (____)
__   (____)
  \__(__)
"""

paper = """
    ____
___/  __)___
        ____)
       ______)
__   ______)
  \______)
"""

scissors = """
    ____
___/  __)___
        ____)
       ______)
__   (___)
  \__(__)
"""

draw = """
# # # # # # # # # # # # # #
#                         #
#       ITS A DRAW!       #
#                         #
# # # # # # # # # # # # # #
"""

win = """
# # # # # # # # # # # # # #
#                         #
#        YOU  WIN!        #
#                         #
# # # # # # # # # # # # # #
"""

loose = """
# # # # # # # # # # # # # #
#                         #
#        YOU LOOSE!       #
#                         #
# # # # # # # # # # # # # #
"""


options = ['r', 'p', 's'] # options for only the cpu
player1 = 'CPU'
game_started = True
game_data = {'r': {'option': 'Rock', 'image': rock}, 'p': {'option': 'Paper', 'image': paper}, 's': {'option': 'Scissors', 'image': scissors}}

def getOption(player_option):
    return game_data[player_option]['option']

def getImage(player_option):
    return game_data[player_option]['image']


# start game
print('Rock Paper Scissors Game\n')
player2 = input('Enter your name: ')
print(player1 + ' vs ' + player2 + '(You)')

while(game_started):
    print('\nGame Menu')
    print('"R" for Rock')
    print('"P" for Paper')
    print('"S" for Scissors\n')

    # get user input and convert it to lowercase character
    cpu = random.choice(options)
    user = input('Choose: ')
    user = user.lower()
    info = f'   {player2} ({getOption(user)}) : CPU ({getOption(cpu)})   '

    if user != 'r' and user != 'p' and user != 's':
        print('Invalid option! Try again.')
        continue

    sleep(1)
    print(f"Your move:{getImage(user)} \n CPU's move:{getImage(cpu)}")

    print('#' * len(info))
    print(f'{info}')
    print('#' * len(info))

    sleep(1)

    # game logic/condition for user to win
    user_wins = ((user == 'r') and (cpu == 's')) or ((user == 'p') and (cpu == 'r')) or ((user == 's') and (cpu == 'p'))

    # game login/condition for cpu to win
    cpu_wins = ((cpu == 'r') and (user == 's')) or ((cpu == 'p') and (user == 'r')) or ((cpu == 's') and (user == 'p'))

    if (getOption(user) == getOption(cpu)):
        print(draw)
        print('Pick again!')
        continue

    elif user_wins:
        print(win)
        game_started = False

    elif cpu_wins:
        print(loose)
        game_started = False

    else:
        print('Invalid option! Try again.')
        continue
